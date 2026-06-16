# Job: DW_StoreDimETL--CopyStoreDimOnly

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DW_StoreDimETL--CopyStoreDimOnly"]
    JOB --> StoreDimETL_1["Step 1: StoreDimETL [SSIS]"]`n```

## Steps

### Step 1: StoreDimETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\StoreDimETL\StoreDimETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10033 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


