# Job: PromotionLocationsToSalesforceCore

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PromotionLocationsToSalesforceCore"]
    JOB --> PromotionLocationsToSalesforceCore_1["Step 1: PromotionLocationsToSalesforceCore [SSIS]"]`n```

## Steps

### Step 1: PromotionLocationsToSalesforceCore
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\POS\PromotionLocationsToSalesforceCore\PromotionLocationsToSalesforceCore.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10181 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


