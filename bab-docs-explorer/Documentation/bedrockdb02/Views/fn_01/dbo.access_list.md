# dbo.access_list

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.access_list"]
    dbo_FNDTN_SCRTY_ACS_LIST(["dbo.FNDTN_SCRTY_ACS_LIST"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_ACS_LIST |

## View Code

```sql
CREATE VIEW dbo.access_list (access_id,access_id_type,app_id,comp_id,ackey,ackey_level)
AS SELECT ACS_ID,ACS_ID_TYPE,APP_ID,CMPNY_ID,ACS_KEY,ACS_KEY_LVL
FROM dbo.FNDTN_SCRTY_ACS_LIST
```

