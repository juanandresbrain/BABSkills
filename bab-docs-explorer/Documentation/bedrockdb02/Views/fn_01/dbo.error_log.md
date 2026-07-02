# dbo.error_log

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.error_log"]
    dbo_FNDTN_SCRTY_ERR_LOG(["dbo.FNDTN_SCRTY_ERR_LOG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_ERR_LOG |

## View Code

```sql
CREATE VIEW dbo.error_log (app_id,comp_id,user_id,user_id_type,instance,time_stamp,error_no,severity_level,error_source,error_message)
AS SELECT APP_ID,CMPNY_ID,USER_ID,USER_ID_TYPE,INSTNC,TIME_STMP,ERR_NUM,SVRTY_LVL,ERR_SRC,ERR_MSG
FROM dbo.FNDTN_SCRTY_ERR_LOG
```

