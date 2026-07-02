# Job: MERCHANDISING - Report - Supplies

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email with supply data

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Supplies"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportSupplies
```


