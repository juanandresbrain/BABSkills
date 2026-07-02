# Job: WEB-Prod-SalesAuditTranslate

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod-SalesAuditTranslate"]
    JOB --> EXEC_WM_spUpdateBrokenOrderItems_1["Step 1: EXEC WM.spUpdateBrokenOrderItems [TSQL]"]`n    JOB --> EXEC_WM_spUpdateChannelAdvisorSets_2["Step 2: EXEC WM.spUpdateChannelAdvisorSets [TSQL]"]`n    JOB --> Download_Transactions_from_Deck_3["Step 3: Download Transactions from Deck [SSIS]"]`n    JOB --> Load_data_to_Sales_Audit_4["Step 4: Load data to Sales Audit [SSIS]"]`n    JOB --> EXEC_spUpdateBrokenInStoreFulfillmentOrders_5["Step 5: EXEC spUpdateBrokenInStoreFulfillmentOrders [TSQL]"]`n```

## Steps

### Step 1: EXEC WM.spUpdateBrokenOrderItems
**Subsystem:** TSQL  

```sql
EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].WebOrderProcessing.WM.spUpdateBrokenOrderItems 
```

### Step 2: EXEC WM.spUpdateChannelAdvisorSets
**Subsystem:** TSQL  

```sql
EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].WebOrderProcessing.WM.spUpdateChannelAdvisorSets
```

### Step 3: Download Transactions from Deck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\OMSTransactionDetailImport.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: Load data to Sales Audit
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\SalesAuditTranslateFromOMS.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"BatchOrderCount(Int32)\"";50 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: EXEC spUpdateBrokenInStoreFulfillmentOrders
**Subsystem:** TSQL  

```sql
EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].[WebOrderProcessing].[WM].[spUpdateBrokenInStoreFulfillmentOrders]
```


