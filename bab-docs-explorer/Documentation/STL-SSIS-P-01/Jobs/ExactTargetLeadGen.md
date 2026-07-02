# Job: ExactTargetLeadGen

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Processed LeadGen file from Exact Target FTP server and loads data to DW.CustomerLeadGen

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ExactTargetLeadGen"]
    JOB --> ExactTargetLeadGen_1["Step 1: ExactTargetLeadGen [SSIS]"]`n```

## Steps

### Step 1: ExactTargetLeadGen
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\ExactTargetLeadGen\ExactTargetLeadGen.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10138 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


