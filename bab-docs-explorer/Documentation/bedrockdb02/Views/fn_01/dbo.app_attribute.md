# dbo.app_attribute

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.app_attribute"]
    dbo_FNDTN_SCRTY_APP_ATRBT(["dbo.FNDTN_SCRTY_APP_ATRBT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_APP_ATRBT |

## View Code

```sql
CREATE VIEW dbo.app_attribute (app_id,app_attrib_id,app_attrib_name, app_attrib_description, app_attrib_mask,
app_attrib_cliptext,app_attrib_required,app_attrib_encrypted)
AS SELECT APP_ID,APP_ATRBT_ID,APP_ATRBT_NAME, APP_ATRBT_DESC,APP_ATRBT_MASK, 
APP_ATRBT_CLIP_TEXT,APP_ATRBT_RQRD, APP_ATRBT_ENCRPTD
FROM dbo.FNDTN_SCRTY_APP_ATRBT
```

