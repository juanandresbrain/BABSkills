# Job: WEB - ProductCatalogExports

**Enabled:** Yes  
**Description:** Previously used to push the catalog data to SalesForce Commerce cloud, is now being used to keep staging that data, but not pushing to Salesforce, but is used for another push to PIM.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - ProductCatalogExports"]
    JOB --> MasterCatalog_1["Step 1: MasterCatalog [SSIS]"]`n    JOB --> JobCompletionNotice_2["Step 2: JobCompletionNotice [TSQL]"]`n```

## Steps

### Step 1: MasterCatalog
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebProductCatalogMaster\WebCatalogMaster.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10055 /Par LoadType;FULL /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: JobCompletionNotice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Web Product Catalog Exports',   @SQLAgent = 'WebProductCatalogExports',  @Recipients = 'BIAdmin@buildabear.com'
```


