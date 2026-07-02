# Job: Zretired_CustomerXMLExtract

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Zretired_CustomerXMLExtract"]
    JOB --> CustomerXMLExtract_1["Step 1: CustomerXMLExtract [SSIS]"]`n```

## Steps

### Step 1: CustomerXMLExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\CustomerXMLExtract\CustomerXML.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


