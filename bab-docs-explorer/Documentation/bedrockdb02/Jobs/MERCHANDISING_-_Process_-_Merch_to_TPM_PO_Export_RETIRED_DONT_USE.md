# Job: MERCHANDISING - Process - Merch to TPM PO Export_RETIRED_DONT_USE

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Exports PO XML files from Merchandising to TPM

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to TPM PO Export_RETIRED_DONT_USE"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputTPMPoXML
```


