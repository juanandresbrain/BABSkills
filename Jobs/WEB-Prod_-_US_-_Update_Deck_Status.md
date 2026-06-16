# Job: WEB-Prod - US - Update Deck Status

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod - US - Update Deck Status"]
    JOB --> Pick_Ticket_PartyID_Merge_1["Step 1: Pick Ticket PartyID Merge [TSQL]"]`n    JOB --> Update_Order_Status_2["Step 2: Update Order Status [SSIS]"]`n    JOB --> EXEC_WMS_spUpdateReleaseDateAndTime_3["Step 3: EXEC WMS.spUpdateReleaseDateAndTime [TSQL]"]`n    JOB --> EXEC_WMS_spRetryReleasedOutOfOrderWaves_4["Step 4: EXEC WMS.spRetryReleasedOutOfOrderWaves [TSQL]"]`n    JOB --> PrintingDataValidation_5["Step 5: PrintingDataValidation [SSIS]"]`n```

## Steps

### Step 1: Pick Ticket PartyID Merge
**Subsystem:** TSQL  

```sql
EXEC [CLB-SQL-P-01].[BABWOrderManagement].[WM].[spPickTicketPartyIDMerge]
```

### Step 2: Update Order Status
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\UpdateDeckStatus.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 6 /Par PickTicketPrintingExe;"\"\\stl-ssis-p-01\d$\ETL Executables\PickTicketPrinting\PickTicketPrinting.exe\"" /Par WOPUpdateDeckStatusExe;"\"\\stl-ssis-p-01\d$\ETL Executables\WOPUpdateDeckStatus\WOPUpdateDeckStatus.exe\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: EXEC WMS.spUpdateReleaseDateAndTime
**Subsystem:** TSQL  

```sql
EXEC IntegrationStaging.WMS.spUpdateReleaseDateAndTime
```

### Step 4: EXEC WMS.spRetryReleasedOutOfOrderWaves
**Subsystem:** TSQL  

```sql
EXEC IntegrationStaging.WMS.spRetryReleasedOutOfOrderWaves
```

### Step 5: PrintingDataValidation
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebPrintingValidations\PrintingValidations.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10037 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


