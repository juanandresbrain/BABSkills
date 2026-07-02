# MerchandisingPlanning.spTXTDataLoad_RunTimeCheck

**Database:** TXTStaging  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_RunTimeCheck"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_sysjobactivity(["dbo.sysjobactivity"]) --> SP
    dbo_sysjobhistory(["dbo.sysjobhistory"]) --> SP
    dbo_sysjobs_view(["dbo.sysjobs_view"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |
| dbo.sysjobactivity |
| dbo.sysjobhistory |
| dbo.sysjobs_view |

## Stored Procedure Code

```sql
-- =============================================
```

