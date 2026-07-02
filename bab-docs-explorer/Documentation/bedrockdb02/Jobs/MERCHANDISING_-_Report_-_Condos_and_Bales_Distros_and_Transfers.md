# Job: MERCHANDISING - Report - Condos and Bales Distros and Transfers

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends and email with CSV attachment to report on Condos and Bales distros exported 'today' to 980 or 960, and pool point condo/bale transfers generated 'today'

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Condos and Bales Distros and Transfers"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectCondosBalesDistrosAndTransfers
```


