## POST /v1/lease

**Headers:**

//found on www.pezapp.io

X-API-KEY = xxx2d4e9-xxxx-xxxx-xxxx-72e348984xxx

**Request Body:**

```
{
   "lease_id":"507f1f77bcf86cd799439011",
   "inventory_id":"507f1f77bcf86cd799439012",
   "username":"joe@user.net",
   "sku":"2c.small",
   "lease_duration":20,
   "lease_end_date":1445444091104630742,
   "lease_start_date":1443716162823973542,
   "procurement_meta":{
      "template_name":"PCFaaS-Slot-10",
      "vcd_username":"vcdUser",
      "vcd_password":"p@55w3rd",
      "base_uri":"vcd.my.fake.cloud.com"
   }
}
```

**Success Response StatusCode:**
201

**Response Body:**

```
{
  "lease_id": "507f1f77bcf86cd799439011",
  "inventory_id": "507f1f77bcf86cd799439012",
  "username": "joe@user.net",
  "sku": "2c.small",
  "lease_duration": 20,
  "lease_end_date": 1445444091104630742,
  "lease_start_date": 1443716162823973542,
  "procurement_meta":{
      "template_name":"PCFaaS-Slot-10",
      "vcd_username":"vcdUser",
      "vcd_password":"p@55w3rd",
      "base_uri":"vcd.my.fake.cloud.com"
   },
  "task": {
    "ID": "560ede8bfccecc0072000001",
    "Timestamp": 1443815051336165844,
    "Expires": 0,
    "Status": "complete",
    "Profile": "longpoll_queue",
    "CallerName": "2c.small",
    "MetaData": {
      "credentials": {
        "app_manager": {
          "cf_cli": {
            "pass": "pivotal",
            "url": "api.pcfaas-slot10.pez.pivotal.io",
            "user": "admin"
          },
          "console_ui": {
            "pass": "pivotal",
            "url": "https://opsmgr.pcfaas-slot10.pez.pivotal.io:443",
            "user": "admin"
          }
        },
        "ops_manager": {
          "admin_ui": {
            "pass": "pivotal",
            "url": "https://opsmgr.pcfaas-slot10.pez.pivotal.io:8443",
            "user": "admin"
          },
          "ssh": {
            "pass": "pivotal",
            "url": "opsmgr.pcfaas-slot10.pez.pivotal.io:22",
            "user": "ubuntu"
          }
        }
      }
    }
  }
}
```
