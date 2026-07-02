# Job: MERCHANDISING - Unreceived Pool Point Transfers

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures unreceived transfers older than 2 days, sends email to distro team

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Unreceived Pool Point Transfers"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectUnreceivedTransfers
```


