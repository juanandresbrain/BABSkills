# Job: MERCHANDISING - Process - Merch to WM Store Master XML

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Runs Store Master export from Merch to WM

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to WM Store Master XML"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputStoreMasterXML
```


