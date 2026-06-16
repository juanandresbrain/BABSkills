# Job: WEB-Prod - Load From OMS

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod - Load From OMS"]
    JOB --> Aptos_ES_to_Deck_OMS_1["Step 1: Aptos ES to Deck OMS [SSIS]"]`n    JOB --> Import_Orders_From_Deck_2["Step 2: Import Orders From Deck [SSIS]"]`n    JOB --> Set_Shipped_3["Step 3: Set Shipped [SSIS]"]`n```

## Steps

### Step 1: Aptos ES to Deck OMS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\AptosEStoDeckOMS.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Import Orders From Deck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\ImportOMS.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 6 /Par WOPSendOrdersToD365Exe;"\"\\stl-ssis-p-01\d$\ETL Executables\WOPSendOrdersToD365\WOPSendOrdersToD365.exe\"" /Par WOPSendOrdersToD365ThreadCount;12 /Par "\"CM.STL-SSIS-T-01.IntegrationStaging 1.ConnectionString\"";"\"Data Source=STL-SSIS-p-01;Initial Catalog=IntegrationStaging;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"CM.STL-SSIS-T-01.IntegrationStaging.ConnectionString\"";"\"Data Source=STL-SSIS-p-01;Initial Catalog=IntegrationStaging;Integrated Security=True;Application Name=SSIS-ImportOMS-{8A09B2FD-8A9B-49DA-B2DC-DB44053A2A07}STL-SSIS-T-01.IntegrationStaging;\"" /Par "\"CM.bedrockdb02.esell.ConnectionString\"";"\"Data Source=bedrockdb02;Initial Catalog=esell;Provider=SQLNCLI11.1;Integrated Security=SSPI;Auto Translate=False;\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Set Shipped
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\setShipped.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


