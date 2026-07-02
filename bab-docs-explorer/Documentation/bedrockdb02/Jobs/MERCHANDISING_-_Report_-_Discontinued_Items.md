# Job: MERCHANDISING - Report - Discontinued Items

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email to report discontinued items

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Discontinued Items"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.SPMerchandisingReportDiscontinuedItem
```


