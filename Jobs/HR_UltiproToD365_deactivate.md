# Job: HR_UltiproToD365_deactivate

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_UltiproToD365_deactivate"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n    JOB --> wait_2["Step 2: wait [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiproToD365_deactivate\HR_UltiproToD365_deactivate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"DynamicsAPI_PathToTokenFile\"";"\"\\stl-ssis-p-01\integrationstaging\DynamicsAPITokens\PROD\OAuthTokens.tok\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"ME_01_ServerName\"";bedrockdb02 /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"WMS_PackageAPI_GetBlobURL\"";"\"https://buildabear.operations.dynamics.com/data/DataManagementDefinitionGroups/Microsoft.Dynamics.DataEntities.GetAzureWriteUrl\"" /Par "\"WMS_PackageAPI_GetSummaryStatusURL\"";"\"https://buildabear.operations.dynamics.com/data/DataManagementDefinitionGroups/Microsoft.Dynamics.DataEntities.GetExecutionSummaryStatus\"" /Par "\"WMS_PackageAPI_StaticPackageFilesPath\"";"\"\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\\"" /Par "\"WMS_PackageAPI_TriggerImportURL\"";"\"https://buildabear.operations.dynamics.com/data/DataManagementDefinitionGroups/Microsoft.Dynamics.DataEntities.ImportFromPackage\"" /Par "\"WMS_TokenFilePassword\"";bearemy /Par "\"WMS_UserCreateBlobDefinitionGroupID\"";MobileDeviceUserDeactivate /Par "\"WMS_UserCreateFileStageLocation\"";"\"\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\\"" /Par "\"WMS_UserCreateLoadType\"";DELTA /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: wait
**Subsystem:** TSQL  

```sql
waitfor delay '00:00:05'
```


