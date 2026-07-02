# dbo.comp_ackey_lockout

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.comp_ackey_lockout"]
    dbo_FNDTN_SCRTY_CMPNY_ACS_KEY_LCKT(["dbo.FNDTN_SCRTY_CMPNY_ACS_KEY_LCKT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_CMPNY_ACS_KEY_LCKT |

## View Code

```sql
CREATE VIEW dbo.comp_ackey_lockout (comp_id,app_id,ackey,reason)
AS SELECT CMPNY_ID,APP_ID,ACS_KEY,LCKT_RSN
FROM dbo.FNDTN_SCRTY_CMPNY_ACS_KEY_LCKT
```

