# dbo.app_comp_property

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.app_comp_property"]
    dbo_FNDTN_SCRTY_APP_CMPNY_PRPRTY(["dbo.FNDTN_SCRTY_APP_CMPNY_PRPRTY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_APP_CMPNY_PRPRTY |

## View Code

```sql
CREATE VIEW dbo.app_comp_property  (app_id, comp_id,nt_map,nt_map_history,nt_map_level,error_logging,error_logging_level,
app_lockout,ackey_lockout,message_port,allow_multi_instance)
AS SELECT APP_ID,CMPNY_ID,NT_MAP,NT_MAP_HSTRY,NT_MAP_LVL,ERR_LOG,ERR_LOG_LVL,
APP_LCKT,ACS_KEY_LCKT,MSG_PORT,ALW_MLTI_INSTNCE
FROM dbo.FNDTN_SCRTY_APP_CMPNY_PRPRTY
```

