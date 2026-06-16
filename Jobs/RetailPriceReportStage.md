# Job: RetailPriceReportStage

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["RetailPriceReportStage"]
    JOB --> RetailPriceReportStage_1["Step 1: RetailPriceReportStage [SSIS]"]`n```

## Steps

### Step 1: RetailPriceReportStage
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Merch\RetailPriceReportStage\RetailPriceReportStage.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10054 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


