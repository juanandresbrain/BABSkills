# dbo.comp_app_attribute

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.comp_app_attribute"]
    dbo_FNDTN_SCRTY_CMPNY_APP_ATRBT(["dbo.FNDTN_SCRTY_CMPNY_APP_ATRBT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_CMPNY_APP_ATRBT |

## View Code

```sql
CREATE VIEW dbo.comp_app_attribute (comp_id,app_id,app_attrib_id,app_attrib_value)
AS SELECT CMPNY_ID,APP_ID,APP_ATRBT_ID,APP_ATRBT_VAL
FROM dbo.FNDTN_SCRTY_CMPNY_APP_ATRBT
```

