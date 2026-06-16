# Job: HR_UltiproToD365

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_UltiproToD365"]
    JOB --> recurring_1["Step 1: recurring [SSIS]"]`n```

## Steps

### Step 1: recurring
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiproToD365\HR_UltiproToD365.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"DynamicsAPI_PathToTokenFile\"";"\"\\stl-ssis-p-01\integrationstaging\DynamicsAPITokens\PROD\OAuthTokens.tok\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"ME_01_ServerName\"";bedrockdb02 /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"WMS_PackageAPI_GetBlobURL\"";"\"https://buildabear.operations.dynamics.com/data/DataManagementDefinitionGroups/Microsoft.Dynamics.DataEntities.GetAzureWriteUrl\"" /Par "\"WMS_PackageAPI_GetSummaryStatusURL\"";"\"https://buildabear.operations.dynamics.com/data/DataManagementDefinitionGroups/Microsoft.Dynamics.DataEntities.GetExecutionSummaryStatus\"" /Par "\"WMS_PackageAPI_StaticPackageFilesPath\"";"\"\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\\"" /Par "\"WMS_PackageAPI_TriggerImportURL\"";"\"https://buildabear.operations.dynamics.com/data/DataManagementDefinitionGroups/Microsoft.Dynamics.DataEntities.ImportFromPackage\"" /Par "\"WMS_TokenFilePassword\"";bearemy /Par "\"WMS_UserCreateFileStageLocation\"";"\"\\stl-ssis-p-01\\IntegrationStaging\\Dynamics\\WarehouseInterfaces\\UserCreate\\\"" /Par "\"WMS_UserCreateLoadType\"";DELTA /Par "\"WMS_UserDeactivateFileStageLocation\"";"\"\\stl-ssis-p-01\\IntegrationStaging\\Dynamics\\WarehouseInterfaces\\UserDeactivate\\\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


