# Job: MERCHANDISING - Process - Rebuild Style List

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Rebuilds keith_wm_style_list table

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Rebuild Style List"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.SPMerchandisingMewVsWMComparison
```


