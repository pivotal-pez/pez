#potential inventory items

## naming format
  * [tier][type].[size]
  * ex. 2A.small would be a pivotalcf install living on open stack of a small footprint.
  
## sizing
  * 2C.small - 128GB ram / 250GB storage / 2 routable IPs 

## tiers
  * 1 heritage - org access on a pivotalcf (only org level control, no ops manager control)
  * 2 PaaS - only access to the paas level (no iaas visibility or control)
  * 3 IaaS - iaas access and up (no visibility to the metal)
  * 4 MaaS - metal and up (I configure and control everything from real server on up ) I get a cluster of metal with some layer of orchestration tied to it.

## types
  * A OpenStack 
  * B vSphere
  * C vCloud
  * D Raw Hardware
  * E Orchestration Layer

## Offerings

* (1) Heritage - I get an org on a pcf instance

* (2) PaaS as the consumable - I get a pre-stoodup PivotalCF foundation of my very own
  * (2C) vCloud - I get a pre-stoodup PivotalCF foundation running on vCloud

* (3) IaaS (VMs as the consumable) - I get my own IaaS to spin up VMs, networking, etc on
  * (3A) OpenStack Org - I get my very own OpenStack Org to use however i wish
  * (3C) vCloudDirector Org - I get my very own vCloudDirector Org to use however i wish

* (4) MaaS - I get my own bare metal set of servers to do whatever i want with
  * (4D) Raw metal - i get some servers
  * (4E) Raw metal + Josh's Python - I get some servers with OSes installed

## possible inventory object structure
```
inventory
{
 sku: 2C.small,
 _id: kaasd9sd9-98239h23h9-99h3ba993ba9h3ab,
 tier: 2,
 type: C,
 size: small,
 attributes: [
  vCloud,
  PivotalCF,
  128GB ram,
  250GB storage,
  2 routable IPs,
 ]
 item_status: leased #[rebuilding, leased, available, maintenance, archiving, reserving], 
 lease-guid:917397-292735-98293752935
}

// for current real lease object structure go here: https://github.com/pivotal-pez/pezdispenser/blob/develop/service/type.go
lease
{
   "_id":"leaseguid",
   "inventory_id":"_id of specific inventory item",
   "username":"joe@user.net",
   "sku":"2c.small",
   "lease_duration":14,
   "lease_end_date":"2000-01-10",
   "lease_start_date":"2000-01-10",
   "consumer_meta":{
      // this should be decorated content added by the dispenser ex.
		    "foundation_username":"admin",
      "foundation_password":"supersecre",
      "foundation_url":"www.gohere.com"      ...
   },
   "procurement_meta":{
      // this is the details required to take procurement actions
		    "template_name":"PCFaaS-Slot-10",
      "vcd_username":"vcdUser",
      "vcd_password":"p@55w3rd",
      "vapp_id":"302172350236723602367"
   },
   "task: {
   		 // this should be decorated content added by the dispenser, but structured Task data
   		 "_id":"mytaskguid",
      "status":"unavailable"   ...
   }
}

```

## inventory service call flow
 * Query inventory service for available items of a particular sku
 * Query inventory service asking for a lease on a particular sku
   * Inventory service updates item_status to a reserving state
   * Inventory service creates a new lease record
   * Inventory service updates lease-guid with the newly created lease record
   * Inventory calls dispenser with a post of the lease object
   * Inventory parses dispenser response, updates lease record, and updates inventry item record
   * client that called inventory service gets the lease object as their response

## dispenser call flow for lease post
 * dispenser recieves post of lease object
  * validate user is allowed to aquire lease of intentory item
  * vend item (wtf does that mean :) )
  * return the decorated lease object as part of a composed response object w/ an added status and potential error message

##NOTE:
* requires out of band event driven stuff, to clean up the reclaimed, previously leased items. this will not only clean the actual item of guid X but update the items record with proper state on success, failure, etc status.

* above flow works for lease and unlease flow, just more or less in reverse.


## Responsibilities

1. Maintain Inventory
2. Manage Leases

### Inventory Admin APIs
```
GET    /admin/products                    # return all products
GET    /admin/product/:id                 # return product details
POST   /admin/product                    # create new product record
POST   /lease/product/:sku                 # create new lease object with given information
PUT    /admin/product/:id                # update product
DELETE /admin/product/:id                # delete product
```

### Dispenser Routes
```
POST   /lease                           # post a lease object to dispenser and recieve a decorated lease response (decorated meaning it should have some creds or info in there)
DELETE /lease                           # delete the given lease object (decomission a given item, tear down, restock)

```

### Portal Routes
```
GET   /products                           # return list of product SKUs

```
