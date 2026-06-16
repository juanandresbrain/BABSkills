# Job: WEB - PricebookExport - Feedonomics

**Enabled:** Yes  
**Description:** Exports Full Load List Price XML files to Feedonomics SFTP for both UK and US webstores

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PricebookExport - Feedonomics"]
    JOB --> SSIS___WebPricebook_1["Step 1: SSIS - WebPricebook [SSIS]"]`n```

## Steps

### Step 1: SSIS - WebPricebook
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebPricebook\WebPricebook.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10151 /Par DestinationSystem;Feedonomics /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";1 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


