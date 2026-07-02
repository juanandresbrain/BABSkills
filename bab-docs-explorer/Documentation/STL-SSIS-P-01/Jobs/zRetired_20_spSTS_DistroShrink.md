# Job: zRetired_20 spSTS_DistroShrink

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_20 spSTS_DistroShrink"]
    JOB --> Step_1_1["Step 1: Step 1 [TSQL]"]`n```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec  [kodiaktest].[BearData].[dbo].[spSTS_DistroShrink]  exec [kodiaktest].[BearData].[dbo].[spSTS_DistroShrinkEmail]
```


