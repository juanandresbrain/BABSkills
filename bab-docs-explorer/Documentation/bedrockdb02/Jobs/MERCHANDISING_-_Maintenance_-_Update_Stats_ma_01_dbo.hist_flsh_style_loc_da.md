# Job: MERCHANDISING - Maintenance - Update Stats ma_01.dbo.hist_flsh_style_loc_da

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Run update statistics ma_01.dbo.hist_flsh_style_loc_da

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Maintenance - Update Stats ma_01.dbo.hist_flsh_style_loc_da"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
update statistics ma_01.dbo.hist_flsh_style_loc_da
```


