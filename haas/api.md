# Innkeeper

All API calls require:
- `Content-Type` - {"Content-Type":"application/json"}
- `Authorization` - Basic Authentication

Available Endpoints:
* [`/v2/Provision`] — Provision an environment

---

## `/v2/Provision`

Add a new post to Delicious.

### Arguments

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
