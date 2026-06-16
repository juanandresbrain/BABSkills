# Job: zRetired_StoreForcePOSSalesExport_MergeAndFileOnly

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_StoreForcePOSSalesExport_MergeAndFileOnly"]
    JOB --> Merge_and_File_Only_1["Step 1: Merge and File Only [SSIS]"]`n```

## Steps

### Step 1: Merge and File Only
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\StoreForce\HR_StoreForcePosSalesExtract\HR_StoreForcePosSalesExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10041 /Par "\"DaysToGoBack(Int32)\"";0 /Par "\"DaysToInclude(Int32)\"";0 /Par StoreForcePOSSalesExtractRunType;MergeAndFileOnly /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


