# dbo.admin_user

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.admin_user"]
    dbo_FNDTN_SCRTY_ADMN_USER(["dbo.FNDTN_SCRTY_ADMN_USER"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_ADMN_USER |

## View Code

```sql
CREATE VIEW dbo.admin_user (app_id,comp_id,user_id)
AS SELECT APP_ID,CMPNY_ID,USER_ID
FROM dbo.FNDTN_SCRTY_ADMN_USER
```

