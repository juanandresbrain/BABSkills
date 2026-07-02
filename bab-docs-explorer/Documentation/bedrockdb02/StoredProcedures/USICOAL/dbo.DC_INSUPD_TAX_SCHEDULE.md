# dbo.DC_INSUPD_TAX_SCHEDULE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INSUPD_TAX_SCHEDULE"]
    dbo_DC_TAX_SCHEDULE(["dbo.DC_TAX_SCHEDULE"]) --> SP
    dbo_TAX_RULE(["dbo.TAX_RULE"]) --> SP
    dbo_TAX_SCHEDULE(["dbo.TAX_SCHEDULE"]) --> SP
    dbo_TMP_TAX_SCHEDULE(["dbo.TMP_TAX_SCHEDULE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_SCHEDULE |
| dbo.TAX_RULE |
| dbo.TAX_SCHEDULE |
| dbo.TMP_TAX_SCHEDULE |

## Stored Procedure Code

```sql

```

