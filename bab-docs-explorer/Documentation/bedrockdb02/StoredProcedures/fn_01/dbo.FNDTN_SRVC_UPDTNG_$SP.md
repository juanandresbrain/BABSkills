# dbo.FNDTN_SRVC_UPDTNG_$SP

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SRVC_UPDTNG_$SP"]
    dbo_FNDTN_SRVC_EXEC(["dbo.FNDTN_SRVC_EXEC"]) --> SP
    dbo_FNDTN_SRVC_MGR_SRVC(["dbo.FNDTN_SRVC_MGR_SRVC"]) --> SP
    dbo_T_INTEGER(["dbo.T_INTEGER"]) --> SP
    dbo_T_LONG_INTEGER(["dbo.T_LONG_INTEGER"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SRVC_EXEC |
| dbo.FNDTN_SRVC_MGR_SRVC |
| dbo.T_INTEGER |
| dbo.T_LONG_INTEGER |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[FNDTN_SRVC_UPDTNG_$SP]
```

