# Job: POS_ProductDataExtract

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["POS_ProductDataExtract"]
    JOB --> SSIS___POS_ProductDataHardLaunchItems_1["Step 1: SSIS - POS_ProductDataHardLaunchItems [SSIS]"]`n    JOB --> POS_ProductDataExtract_2["Step 2: POS_ProductDataExtract [SSIS]"]`n    JOB --> Load_Product_Table_for_Power_BI__non_POS_items__3["Step 3: Load Product Table for Power BI (non POS items) [SSIS]"]`n    JOB --> POS_ProductImageURLNamesDescriptions_4["Step 4: POS_ProductImageURLNamesDescriptions [SSIS]"]`n    JOB --> Load_Products_to_WebOrderProcessing_for_Mulesoft_Sales_Extract_5["Step 5: Load Products to WebOrderProcessing for Mulesoft Sales Extract [TSQL]"]`n    JOB --> Set_POS_Products_Out_of_Stock_6["Step 6: Set POS Products Out of Stock [TSQL]"]`n    JOB --> Job_Completion_Notification_7["Step 7: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: SSIS - POS_ProductDataHardLaunchItems
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\POS\POS_ProductDataHardLaunchItems\POS_ProductDataHardLaunchItems.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10174 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: POS_ProductDataExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\POS\POS_ProductDataExtract\POS_ProductDataExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10160 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Load Product Table for Power BI (non POS items)
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\POS\PBIProductDataExtract\PBIProductDataExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10178 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: POS_ProductImageURLNamesDescriptions
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\POS\POS_ProductImageURLs\POS_ProductImageURLs.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10162 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: Load Products to WebOrderProcessing for Mulesoft Sales Extract
**Subsystem:** TSQL  

```sql
exec [bearcluster01.sql.buildabear.com].WebOrderProcessing.dbo.spMergePOSProducts
```

### Step 6: Set POS Products Out of Stock
**Subsystem:** TSQL  

```sql
exec POS.spMergeProductsOutOfStock
```

### Step 7: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'POS Product Data Extract',   @SQLAgent = 'POS_ProductDataExtract',  @Recipients = 'biadmin@buildabear.com'
```


