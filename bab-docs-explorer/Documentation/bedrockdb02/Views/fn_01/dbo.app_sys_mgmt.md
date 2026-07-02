# dbo.app_sys_mgmt

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.app_sys_mgmt"]
    dbo_FNDTN_SCRTY_APP_SYS_MNGMNT(["dbo.FNDTN_SCRTY_APP_SYS_MNGMNT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_APP_SYS_MNGMNT |

## View Code

```sql
CREATE VIEW dbo.app_sys_mgmt (app_id,mgmt_id)
AS SELECT APP_ID,MNGMNT_ID
FROM dbo.FNDTN_SCRTY_APP_SYS_MNGMNT
```

