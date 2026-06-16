# Job: zRetired_ERP_SupplyProcessing

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ERP_SupplyProcessing"]
    JOB --> 1100_1["Step 1: 1100 [SSIS]"]`n    JOB --> 2110_2["Step 2: 2110 [SSIS]"]`n    JOB --> 1700_3["Step 3: 1700 [SSIS]"]`n    JOB --> 3001_4["Step 4: 3001 [SSIS]"]`n    JOB --> Exec_PFTOpentoBuyProductCategoryAssignments_5["Step 5: Exec PFTOpentoBuyProductCategoryAssignments [SSIS]"]`n```

## Steps

### Step 1: 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERPSuppliesProcessing\PFTOpentoBuy.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$Project::SupplyProcessingIntegrationServer\"";"\"stl-ssis-p-01\"" /Par "\"$Project::CM.IntegrationStaging.ConnectionString\"";"\"Data Source=stl-ssis-p-01;Initial Catalog=IntegrationStaging;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: 2110
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERPSuppliesProcessing\PFTOpentoBuy.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$Project::SupplyProcessingIntegrationServer\"";"\"stl-ssis-p-01\"" /Par "\"$Project::CM.IntegrationStaging.ConnectionString\"";"\"Data Source=stl-ssis-p-01;Initial Catalog=IntegrationStaging;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: 1700
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERPSuppliesProcessing\PFTOpentoBuy.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$Project::SupplyProcessingIntegrationServer\"";"\"stl-ssis-p-01\"" /Par "\"$Project::CM.IntegrationStaging.ConnectionString\"";"\"Data Source=stl-ssis-p-01;Initial Catalog=IntegrationStaging;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1700 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: 3001
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERPSuppliesProcessing\PFTOpentoBuy.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$Project::SupplyProcessingIntegrationServer\"";"\"stl-ssis-p-01\"" /Par "\"$Project::CM.IntegrationStaging.ConnectionString\"";"\"Data Source=stl-ssis-p-01;Initial Catalog=IntegrationStaging;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: Exec PFTOpentoBuyProductCategoryAssignments
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERPSuppliesProcessing\PFTOpentoBuyProductCategoryAssignments.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$Project::SupplyProcessingIntegrationServer\"";"\"stl-ssis-p-01\"" /Par "\"$Project::CM.IntegrationStaging.ConnectionString\"";"\"Data Source=stl-ssis-p-01;Initial Catalog=IntegrationStaging;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


