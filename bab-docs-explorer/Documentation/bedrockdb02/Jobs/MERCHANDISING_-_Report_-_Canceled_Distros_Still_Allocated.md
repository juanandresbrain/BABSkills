# Job: MERCHANDISING - Report - Canceled Distros Still Allocated

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email with distros that are canceled and still have allocated qty

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Canceled Distros Still Allocated"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectCanceledDistros
```


