# Job: HR_Core_ETL

**Enabled:** Yes  
**Description:** Runs Core Data import from file extract out of Ultipro. Merges data into DW tables and Store MDM.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_Core_ETL"]
    JOB --> HR_Core_ETL_1["Step 1: HR_Core_ETL [SSIS]"]`n    JOB --> HR_Sage_ETL_2["Step 2: HR_Sage_ETL [SSIS]"]`n    JOB --> HR_UltiproEmpIDtoAD_3["Step 3: HR_UltiproEmpIDtoAD [SSIS]"]`n    JOB --> HR_ADEmployeeExtract_4["Step 4: HR_ADEmployeeExtract [SSIS]"]`n    JOB --> HR_expiryCLear_5["Step 5: HR_expiryCLear [SSIS]"]`n    JOB --> HR_UltiProToADtoUltiPro_6["Step 6: HR_UltiProToADtoUltiPro [SSIS]"]`n    JOB --> HR_Ultipro_OU_Update_7["Step 7: HR_Ultipro_OU_Update [SSIS]"]`n    JOB --> HR_Sage_ETL2_8["Step 8: HR_Sage_ETL2 [SSIS]"]`n    JOB --> HR_UltiProActivations_9["Step 9: HR_UltiProActivations [SSIS]"]`n```

## Steps

### Step 1: HR_Core_ETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_Core_ETL\HR_Core_ETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"Auditworks_ServerName\"";bedrockdb01 /Par "\"BABWMstrData_Server\"";Kodiak /Par "\"CRM_ServerName\"";"\"STL_CRMDB_P_01\"" /Par "\"DWStaging_ServerName\"";papamart /Par "\"DW_ServerName\"";papamart /Par "\"DaysToGoBack(Int32)\"";1 /Par "\"DaysToInclude(Int32)\"";1 /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"ME_01_ServerName\"";bedrockdb02 /Par "\"Parameter(Int32)\"";0 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: HR_Sage_ETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_Sage_ETL\HR_Sage_ETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: HR_UltiproEmpIDtoAD
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiproEmpIDtoAD\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: HR_ADEmployeeExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_ADEmployeeExtract\HR_ADEmployeeExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10052 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: HR_expiryCLear
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_expiryClear\HR_expiryClear.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: HR_UltiProToADtoUltiPro
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiProToADtoUltiPro\HR_UltiProToADtoUltiPro.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10053 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 7: HR_Ultipro_OU_Update
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_Ultipro_OU_update\HR_Ultipro_OU_update.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 8: HR_Sage_ETL2
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_Sage_ETL2\HR_Sage_ETL_2.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 9: HR_UltiProActivations
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiProActivations\HR_UltiProActivations.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


