# Job: MERCHANDISING - Report - PO Receipt Errors

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checks for po receipt errors logged in the pipeline, sends email

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - PO Receipt Errors"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportPOReceiptErrors
```


