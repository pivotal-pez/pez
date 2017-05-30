# Innkeeper

All API calls require headers:
- `Content-Type` - application/json
- `Authorization` - Basic Authentication

Available Endpoints:
* [`/v2/GetCapacity/{GEO_LOC}/{SKU}`] `GET` Ask for available capacity for a specific sku in a specific location
* [`/v2/GetProductSkus/{GEO_LOC}`] `GET` Ask for all catalog items available in a specific location
* [`/v2/Provision`] `POST` Provision an environment

---


## `/v2/GetCapacity/{GEO_LOC}/{SKU}`

Ask for available capacity for a specific sku in a specific location.

`GET`

### Inline Arguments
- `sku` (required) — The catalog item that is being requested
- `geo_loc` (required) — Geographic location of the environment (PAO, SC2, ORK..)

### Body Arguments

none


### Example Response

If the call was successful:

```json
{
  "sc2.linux.centos72.standard": {
    "Description": "",
    "Type": "linux"
  },
  ...
}
```

## `/v2/GetProductSkus/{GEO_LOC}`

Ask for all catalog items available in a specific datacenter.

`GET`

### Inline Arguments
- `geo_loc` (required) — Geographic location of the environment (PAO, SC2, ORK..)

### Body Arguments

none


### Example Response

If the call was successful:

```json
{
  "sc2.linux.centos72.standard": {
    "Description": "",
    "Type": "linux"
  },
  ...
}
```


## `/v2/Provision`

Request an environment to be provisioned.

`POST`

### Inline Arguments

none

### Body Arguments

- `sku` (required) — The catalog item that is being requested
- `tenantid` (required) — Prefix for what the resulting environment will be called 
- `zone` (required) — Network location for the environment (internal or external)
- `geo_loc` (required) — Geographic location of the environment (PAO, SC2, ORK..)
- `origin` (required) — No longer used, but required
- `buName` (required) — No longer used, but required
- `qualification` (required) — No longer used, but required
- `duration` (required) — No longer used, but required
- `salesforce` (required) — No longer used, but required
- `contact` (required) — No longer used, but required


### Example Response

If the call was successful:

```json
{
  "status": "success",
  "data": [
    {
      "tenantid": "jgray-test-RP8RMG",
      "sku": "sc2.vs.standard",
      "zone": "internal",
      "geo_loc": "SC2",
      "descr": "<b>this is a test.</b> Here is some data<br><br>Here is some more <b>data.</b>"
    }
  ],
  "message": "ok"
}
```

If the call failed:

```json
tbd
```
