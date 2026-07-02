# dbo.NSB_SP_EMPL_FILE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_EMPL_FILE"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_OPR_RSRC_ACCESS(["dbo.OPR_RSRC_ACCESS"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.OPERATOR |
| dbo.OPR_RSRC_ACCESS |
| dbo.RPT_SELECT_OBJECT |

## Stored Procedure Code

```sql
/*Report Id = 1010 */
```

