# Job: zRetired - WEB_UKWebInventory

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** Captures ProdBal for UK Webstore and Stages Data to be picked up for inventory load to Deck OMS.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired - WEB_UKWebInventory"]
    JOB --> UKWebInventory_1["Step 1: UKWebInventory [SSIS]"]`n    JOB --> WebInventoryToDeck_2["Step 2: WebInventoryToDeck [SSIS]"]`n    JOB --> Job_Completion_Notice_3["Step 3: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: UKWebInventory
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\UKWebInventory\UKWebInventory.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10102 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WebInventoryToDeck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebInventory\WebInventory.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10089 /Par "\"LocationID(Int16)\"";2013 /Par "\"WebInventory_LoadDestination\"";WEB /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'UK Web Inventory - Clipper to Deck - Hourly',   @SQLAgent = 'WEB_UKWebInventory',  @Recipients = 'biadmin@buildabear.com'
```


