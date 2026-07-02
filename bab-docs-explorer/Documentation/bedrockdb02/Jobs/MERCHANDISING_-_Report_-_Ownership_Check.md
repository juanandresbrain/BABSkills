# Job: MERCHANDISING - Report - Ownership Check

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email with style ownership info

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Ownership Check"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportOwnershipCheck
```


