# Job: MERCHANDISING - Process - Nightly Sync All Whse and Web

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** compares inventories between Merch and the warehouses, posts a shrink adjustment file for discrepancies, sends emails with summaries.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Nightly Sync All Whse and Web"]
    JOB --> spMerchandisingSelectWhseInventoryShrink_1["Step 1: spMerchandisingSelectWhseInventoryShrink [TSQL]"]`n    JOB --> Trigger_Store_Sync___Dynamics_to_Aptos_2["Step 2: Trigger Store Sync - Dynamics to Aptos [TSQL]"]`n    JOB --> Log_WM_Unselected_Web_Qty_3["Step 3: Log WM Unselected Web Qty [TSQL]"]`n```

## Steps

### Step 1: spMerchandisingSelectWhseInventoryShrink
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectWhseInventoryShrink
```

### Step 2: Trigger Store Sync - Dynamics to Aptos
**Subsystem:** TSQL  

```sql

--EXEC sp_start_job @job_name='MERCHANDISING - NightlySync_Stores_DynamicsToAptos'
-- Replaced Above on 8/31/2023
EXEC [STL-SSIS-P-01].msdb.dbo.sp_start_job @job_name='WMS_NonWarehouseInventoryShrinkToAptos'
```

### Step 3: Log WM Unselected Web Qty
**Subsystem:** TSQL  

```sql
--exec wmdb01.wmprod.dbo.spLogWebOrderUnselectedQty --commented out for WM upgrade
```


