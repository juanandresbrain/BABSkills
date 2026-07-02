# Job: MERCHANDISING - Report - Merchandising Style List

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Emails Style List

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Merchandising Style List"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportStyleList
```


