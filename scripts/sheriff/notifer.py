#!/usr/bin/python

# Author: JGray <jgray@pivotal.io>

import MySQLdb as mdb
# on CentOS, `yum install MySQL-python`

import smtplib
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import urllib
import urllib2



sender = 'pez-sheriff@pivotal.io'
sender_full = 'PEZ Sheriff <pez-sheriff@pivotal.io>'


def logAction(theorg, themessage):
	try:
        	con = mdb.connect('pez-db.core.pao.pez.pivotal.io', 'sheriffuser', '***pw***', 'sheriff');
                cur = con.cursor()

		sql = "INSERT INTO action_log(org, message, thedatetime) VALUES('"+theorg+"', '"+themessage+"', now())"
		cur.execute(sql)

        except mdb.Error, e:

                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)

        finally:

                if con:
                        con.close()



def sendEmail( sender, to, body, subject ):

	tolist = ['josh@jtri.com']
	tolist.append(to)

        message = """From: PEZ Sheriff <pez-sheriff@pivotal.io>
To: PEZ User <pez-user@pivotal.io>
MIME-Version: 1.0
Content-type: text/html
"""


        message += "Subject: "+subject+"\n"
        message += body
        message += "<br><br>---<br>This message has been sent by a PEZ robot, do not reply to this message."

        try:
                smtpObj = smtplib.SMTP('smtp.pivotal.io')
                smtpObj.sendmail(sender, tolist, message)
                print "Successfully sent email"
        except SMTPException:
                print "Error: unable to send email"

	logAction('email', 'sent email with body: '+body)




def main():
	global sender
	global sender_full

	try:
		con = mdb.connect('pez-db.core.pao.pez.pivotal.io', 'sheriffuser', '***pw***', 'sheriff');
		cur = con.cursor()
	 
		#################################################################################
		# (1) Look for VCD tenants that are expiring in less than a week, and not disabled
		cur.execute("SELECT orgname, contactemail, contactnickname, contactfullname, expirydate FROM tenants where ((expirydate < curdate()+7) and expirydate !=curdate()) and type='vcd' and disabled=0")

		rows = cur.fetchall()

		for row in rows:
			orgname = row[0]
			contactemail = row[1]
			contactnickname = row[2]
			contactfullname = row[3]
			expirydate = row[4]
			receivers = [contactemail]
			print "Exipring soon: "+orgname

			body =  "Hello "+contactfullname+", Your Sandbox capacity in vCloud Director '"+orgname+"' is set to <b>expire on "+str(expirydate)+"</b><br><br>Open a ticket with ask@pivotal.io to have your lease extended otherwise it will be torn down on this date."

			subject = "PEZ Service Notice: Expiration of Sandbox Capacity ("+orgname+")"

			sendEmail(sender, contactemail, body, subject)	
			logAction(orgname, 'sent expiry warning email to '+contactemail+' from '+sender)

			#sql = "INSERT INTO action_log(org, message, thedatetime) VALUES('"+orgname+"', 'sent expiry warning email to "+contactemail+"', now())"
			#cur.execute(sql)

		#################################################################################
		# (2) Look for VCD tenants that are expired, begin to teardown
		orgname = ""
		sql = "SELECT orgname FROM tenants where expirydate <= curdate() and type='vcd' and disabled=0 and protected!=1"
		cur.execute(sql)
		rows = cur.fetchall()
		for row in rows:
			orgname = row[0]
			if orgname:
				print "Expired: "+orgname

				body =  "Organization "+orgname+" has been disabled.  It will be destroyed in 7 days.   Well it would be if it was fully automated.  So have someone go do this pleeeease."
				subject = "PEZ Service Notice: Sandbox capacity disabled ("+orgname+")"
				sendEmail(sender, 'jgray@pivotal.io', body, subject)

				# Action: disable row in db, disable org in VCD
				sql = "UPDATE tenants SET disabled = 1 WHERE orgname='"+orgname+"'"
				cur.execute(sql)
				#print sql
				sql = "INSERT INTO action_log(org, message, thedatetime) VALUES('"+orgname+"', 'disabled org in VCD', now())"
				cur.execute(sql)


		#################################################################################
		# (3) Look for VCD tenants that are expired, disabled,and readyto be torn down (1 week past expiry)
		cur.execute("SELECT orgname FROM tenants where expirydate <= curdate()-7 and type='vcd' and disabled=1 and protected!=1")
		rows = cur.fetchall()
		for row in rows:
			orgname = row[0]
			print "Ready for nuking: "+orgname

			body =  "Organization "+orgname+" has been REMOVED.  Well it would be....if we had the API steps worked out.  So someone go do this by hand please."
			subject = "PEZ Service Notice: Sandbox capacity removed ("+orgname+")"
			sendEmail(sender, 'jgray@pivotal.io', body, subject)


			# Action: delete all VCD objects
			sql = "INSERT INTO action_log(org, message, thedatetime) VALUES('"+orgname+"', 'deleted org in VCD', now())"
			cur.execute(sql)


		#################################################################################
                # (4) Look for problems in tenants table
		sql = "SELECT orgname from tenants where (location != 'sandbox-vcd-01')"
		cur.execute(sql)
		rows = cur.fetchall()
                for row in rows:
			orgname = row[0]
			print "PROBLEM: organization "+orgname+" has a mistake in the location field"
			
			body =  "Organization "+orgname+" has a non-existent location in database"
                        subject = "PEZ DB Notice: Org problem ("+orgname+")"
                        sendEmail(sender, 'jgray@pivotal.io', body, subject)



                #################################################################################
                # (5) Look for problems in VCD, like an Org present that is not in DB
		
		#first you get a token
		method = "POST"
		url = 'https://sandbox.pez.pivotal.io/api/sessions'

		password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		password_manager.add_password(None, url, 'administrator@system', '***pw***')
		auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
		handler= urllib2.HTTPHandler()
		opener = urllib2.build_opener(auth_manager)
		headers = {'Accept': 'application/*+xml;version=5.5'}
		values = {}
		data = urllib.urlencode(values)
		request = urllib2.Request(url, data, headers)
		request.add_header = [('Accept', 'application/*+xml;version=5.5')]
		request.get_method = lambda: method
		opener = urllib2.build_opener(auth_manager)
		try:
		    connection = opener.open(request)
		except urllib2.HTTPError,e:
		    connection = e
		if connection.code == 200:
		    data = connection.read()
		else:
		    print "Something is wrong: Code "+str(connection.code)
		token = connection.info().getheader('x-vcloud-authorization')

		url = 'https://sandbox.pez.pivotal.io/api/admin/orgs/query?pageSize=10000000'
		method = "GET"
		handler= urllib2.HTTPHandler()
		opener = urllib2.build_opener(auth_manager)
		headers = dict()
		headers['Accept'] = 'application/*+xml;version=5.5'
		headers['x-vcloud-authorization'] = token

		values = {}
		data = urllib.urlencode(values)
		request = urllib2.Request(url, data, headers)
		request.get_method = lambda: method
		opener = urllib2.build_opener(auth_manager)
		try:
		    connection = opener.open(request)
		except urllib2.HTTPError,e:
		    connection = e

		# check. Substitute with appropriate HTTP code.
		if connection.code == 200:
		    data = connection.read()
		else:
		    print "Something is wrong: Code "+str(connection.code)

		DOMTree = xml.dom.minidom.parseString(data)
		collection = DOMTree.documentElement

		orgs = collection.getElementsByTagName("OrgRecord")

		for org in orgs:
		   if org.hasAttribute("name"):
			#print "org found: "+org.getAttribute("name")
			sql = "SELECT orgname from tenants where (orgname = '"+org.getAttribute("name")+"')"
			cur.execute(sql)
			rows = cur.fetchall()
			for row in rows:
				orgname = row[0]
				#print "Org "+orgname+" is good"
			if len(rows) != 1:
				print "Org "+org.getAttribute("name")+" is in vCD but missing from PEZ DB"
				body =  "Organization "+org.getAttribute("name")+" is in vCD but missing from PEZ DB"
				subject = "PEZ DB Notice: Org problem ("+org.getAttribute("name")+")"
				sendEmail(sender, 'jgray@pivotal.io', body, subject)





	except mdb.Error, e:
	  
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	finally:
	    
		if con:
			con.close()


# END MAIN

main()
