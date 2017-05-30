# Posts

Posts are the atomic building blocks of Delicious. Typically, a Post contains a link and several meta data.

* [`/v1/posts/update`](#v1postsupdate) — Check to see when a user last posted an item.

---

## `/v1/posts/update`

Check to see when a user last posted an item. Returns the last updated time for the user, as well as the number of new items in the user’s inbox since it was last visited.

Use this before calling posts/all to see if the data has changed since the last fetch.

### Example Response

```xml
<update code="200" inboxnew="" message="success" time="2015-01-15T17:35:48Z"/>
```

## `/v1/posts/add?`

Add a new post to Delicious.

### Arguments

- `&url={URL}` (required) — The url of the item.
- `&description={...}` (required) — The description of the item.
- `&extended={...}` (optional) — Notes for the item.
- `&tags={...}` (optional) — Tags for the item (comma delimited).
- `&dt={CCYY-MM-DDThh:mm:ssZ}` (optional) — Datestamp of the item (format “CCYY-MM-DDThh:mm:ssZ”). Requires a LITERAL “T” and “Z” like in ISO8601 at http://www.cl.cam.ac.uk/~mgk25/iso-time.html for Example: `1984-09-01T14:21:31Z`.
- `&replace=no` (optional) — Don’t replace post if given url has already been posted.
- `&shared=no` (optional) — Make the item private.

### Example Response

If the post was successful:

```xml
<result code="done" />
```

If the post failed:

```xml
<result code="something went wrong" />
```
