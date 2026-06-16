# Job: ExchangeRates

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ExchangeRates"]
    JOB --> Load_New_Exchange_Rates_1["Step 1: Load New Exchange Rates [SSIS]"]`n```

## Steps

### Step 1: Load New Exchange Rates
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\Exchange Rate Update\Exchange Rate Upsert.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 24 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


