# Job: Update Statistics - MA_01 - hist_sku_loc_wk

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Update Statistics - MA_01 - hist_sku_loc_wk"]
    JOB --> Step_Uno_1["Step 1: Step Uno [TSQL]"]`n```

## Steps

### Step 1: Step Uno
**Subsystem:** TSQL  

```sql
UPDATE STATISTICS hist_sku_loc_wk
```


