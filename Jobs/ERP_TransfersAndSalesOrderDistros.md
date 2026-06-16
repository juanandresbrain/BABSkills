# Job: ERP_TransfersAndSalesOrderDistros

**Enabled:** No  
**Description:** JOB IS DISABLED, IT IS CALLED FROM SQL JOB WMS_TransferOrderCreateFromAptos

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ERP_TransfersAndSalesOrderDistros"]
    JOB --> WMS_DynamicsTransferAndSalesOrderExtract_1["Step 1: WMS_DynamicsTransferAndSalesOrderExtract [SSIS]"]`n    JOB --> 1100_2["Step 2: 1100 [SSIS]"]`n    JOB --> 1200_3["Step 3: 1200 [SSIS]"]`n    JOB --> 2110_4["Step 4: 2110 [SSIS]"]`n    JOB --> 3001_5["Step 5: 3001 [SSIS]"]`n```

## Steps

### Step 1: WMS_DynamicsTransferAndSalesOrderExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_DynamicsTransferAndSalesOrderExtract\WMS_DynamicsTransferOrderSalesOrderExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10105 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";1 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_TransfersAndSalesOrderDistros\ERP_TransfersAndSalesOrderDistros.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 19 /Par "\"CM.BearData.Password\"";"\"pm_r3p0\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: 1200
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_TransfersAndSalesOrderDistros\ERP_TransfersAndSalesOrderDistros.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 19 /Par "\"CM.BearData.Password\"";"\"pm_r3p0\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1200 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: 2110
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_TransfersAndSalesOrderDistros\ERP_TransfersAndSalesOrderDistros.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 19 /Par "\"CM.BearData.Password\"";"\"pm_r3p0\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: 3001
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_TransfersAndSalesOrderDistros\ERP_TransfersAndSalesOrderDistros.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 19 /Par "\"CM.BearData.Password\"";"\"pm_r3p0\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /CALLERINFO SQLAGENT /REPORTING E
```


