# Job: MERCHANDISING - Report - Min-Max Sunday

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends an email with a total number of min max profiles updated after the min max profiles job runs on Sunday morning.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Min-Max Sunday"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[spMerchandisingMinMaxRunCheck]
```


