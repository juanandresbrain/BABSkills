# Job: MERCHANDISING - Report - Multiple Std Pack Qty

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email for styles with multiple std pack qty

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Multiple Std Pack Qty"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportMultipleStdPackQty
```


