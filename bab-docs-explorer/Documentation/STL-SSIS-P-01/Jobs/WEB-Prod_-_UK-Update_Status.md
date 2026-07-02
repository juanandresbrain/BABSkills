# Job: WEB-Prod - UK-Update Status

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod - UK-Update Status"]
    JOB --> Download_Warehouse_Status_Updates_1["Step 1: Download Warehouse Status Updates [TSQL]"]`n    JOB --> Update_UK_Order_Status_2["Step 2: Update UK Order Status [SSIS]"]`n```

## Steps

### Step 1: Download Warehouse Status Updates
**Subsystem:** TSQL  

```sql
EXEC [WEB].[spFTPukWarehouseOrderStatusUpdate]
```

### Step 2: Update UK Order Status
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\UpDateUKStatus.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 6 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


