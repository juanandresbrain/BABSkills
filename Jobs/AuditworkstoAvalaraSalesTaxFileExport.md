# Job: AuditworkstoAvalaraSalesTaxFileExport

**Enabled:** Yes  
**Description:** Creates Export file for Tax Department for Avalara import for USA and CAN stores

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AuditworkstoAvalaraSalesTaxFileExport"]
    JOB --> SSIS___AuditworkstoAvalaraSalesTaxFileExport_1["Step 1: SSIS - AuditworkstoAvalaraSalesTaxFileExport [SSIS]"]`n```

## Steps

### Step 1: SSIS - AuditworkstoAvalaraSalesTaxFileExport
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\AuditworkstoAvalaraSalesTaxFileExport\AuditworkstoAvalaraSalesTaxFileExport.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10152 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


