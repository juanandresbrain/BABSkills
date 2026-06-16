# Job: WMS_ItemCreate

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ItemCreate"]
    JOB --> WMS_ItemCreate___Extract___All_1["Step 1: WMS_ItemCreate - Extract - All [SSIS]"]`n    JOB --> WMS_ItemCreate___Load_Merch_2["Step 2: WMS_ItemCreate - Load Merch [SSIS]"]`n    JOB --> WMS_ItemCreate___Load_Serv_3["Step 3: WMS_ItemCreate - Load Serv [SSIS]"]`n```

## Steps

### Step 1: WMS_ItemCreate - Extract - All
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ItemCreate\WMS_ItemCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10104 /Par ExtractOrLoad;Extract /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WMS_ItemCreate - Load Merch
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ItemCreate\WMS_ItemCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10104 /Par ExtractOrLoad;Load /Par "\"WMS_ItemCreateMerchVsServ\"";Merch /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: WMS_ItemCreate - Load Serv
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ItemCreate\WMS_ItemCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10104 /Par ExtractOrLoad;Load /Par "\"WMS_ItemCreateMerchVsServ\"";Serv /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


