# Job: zRetired_DatoRamaKeyStoryETL

**Enabled:** No  
**Description:** This job is called by SQL Agent Job: DatoRamaETL_MorningLoad

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_DatoRamaKeyStoryETL"]
    JOB --> DatoRamaKeyStoryETL_1["Step 1: DatoRamaKeyStoryETL [SSIS]"]`n```

## Steps

### Step 1: DatoRamaKeyStoryETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\DatoRamaKeyStoryETL\DatoRamaKeyStoryETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10149 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


