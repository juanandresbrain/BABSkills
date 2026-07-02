# Job: MERCH ADMIN - Check Distro Export

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Calls spMerchandisingDistroExportRunCheck which checks for the last time that MERCHANDISING - Process - Merch to Whse Distro Export completed and sends an alert if it has not run for over an hour.  If the job is not running, there may be an issue with DISTRO EXPORT - DYNAMICS AND MERCH.  If this is the case, the Data Bear team will likely need to be contacted.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCH ADMIN - Check Distro Export"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[spMerchandisingDistroExportRunCheck]
```


