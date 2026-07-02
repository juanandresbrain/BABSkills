# Job: MERCHANDISING - Process - Archive Average Cost

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Rebuilds keith_average_cost table

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Archive Average Cost"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.SPMerchandisingArchiveAverageCost
```


