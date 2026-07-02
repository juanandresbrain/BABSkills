# Job: WEB - IntegrationValidations

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - IntegrationValidations"]
    JOB --> WebIntegrationValidations_1["Step 1: WebIntegrationValidations [SSIS]"]`n```

## Steps

### Step 1: WebIntegrationValidations
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebIntegrationValidations\WebIntegrationValidations.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par ApplicationResourcesServerName;"\"BearCluster01.sql.buildabear.com\"" /Par OMSxmlErrFilePath;"\"\\kermode\FileRepository\OMSOrders\Err\"" /Par ProductionServer;"\"bearcluster01.sql.buildabear.com\"" /Par SalesAuditServer;bedrockdb01 /Par WMDatabase;wmprod /Par WMServerName;wmdb01 /Par "\"CM.auditworks.ConnectionString\"";"\"Data Source=bedrockdb01;Initial Catalog=auditworks;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


