# Job: zRetired_WEB - Google Ads Local Inventory Load

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** Disabled job on 10/2/2023 at the direction of Bryce Ahrens. Since the web upgrade to SFRA in late September 2023  there were no pricebook file exporting from SFCC which this dataset relies on for up to date price information. Bryce advised that he believes this data will be going through Feedonomics.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - Google Ads Local Inventory Load"]
    JOB --> SSIS_Step1____GoogleLocalStoreInventoryFile_1["Step 1: SSIS Step1  - GoogleLocalStoreInventoryFile [SSIS]"]`n```

## Steps

### Step 1: SSIS Step1  - GoogleLocalStoreInventoryFile
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\GoogleLocalStoreInventoryFile\GoogleLocalStoreInventoryFile.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10108 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


