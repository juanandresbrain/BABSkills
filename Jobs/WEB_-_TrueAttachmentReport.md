# Job: WEB - TrueAttachmentReport

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - TrueAttachmentReport"]
    JOB --> SSIS___WebTrueAttachmentReport_1["Step 1: SSIS - WebTrueAttachmentReport [SSIS]"]`n```

## Steps

### Step 1: SSIS - WebTrueAttachmentReport
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebTrueAttachmentReport\WebTrueAttachmentReport.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10155 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


