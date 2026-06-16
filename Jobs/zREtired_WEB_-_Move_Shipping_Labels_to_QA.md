# Job: zREtired_WEB - Move Shipping Labels to QA

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zREtired_WEB - Move Shipping Labels to QA"]
    JOB --> Run_Original_File_Move_Job_that_Works_1["Step 1: Run Original File Move Job that Works [SSIS]"]`n    JOB --> Run_New_File_Move_Job_which_for_Some_reason__File_Move_Does_Not_Work___Access_is_denied_to_wm_folder_2["Step 2: Run New File Move Job which for Some reason, File Move Does Not Work - Access is denied to wm folder [SSIS]"]`n```

## Steps

### Step 1: Run Original File Move Job that Works
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WEBMoveWMShippingLabelSpoolFiles\MoveWMShippingSpoolFiles.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par Environment;prod /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Run New File Move Job which for Some reason, File Move Does Not Work - Access is denied to wm folder
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\MoveWMShippingSpoolFiles.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


