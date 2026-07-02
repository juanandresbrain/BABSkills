# Job: MERCHANDISING - Report SL Last Posting

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Outputs SL last posting data

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report SL Last Posting"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputSLlastPosting
```


