# dbo.sys_mgmt

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sys_mgmt"]
    dbo_FNDTN_SCRTY_SYS_MNGMNT(["dbo.FNDTN_SCRTY_SYS_MNGMNT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_SYS_MNGMNT |

## View Code

```sql
create view  dbo.sys_mgmt (mgmt_id,mgmt_name,mgmt_description)
AS SELECT MNGMNT_ID,MNGMNT_NAME,MNGMNT_DESC
FROM dbo.FNDTN_SCRTY_SYS_MNGMNT
```

