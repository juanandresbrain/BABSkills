# Job: WMS_Report - Email Purchase Order Receipts - Today

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - Email Purchase Order Receipts - Today"]
    JOB --> Check_For_Receipts__execute_SSRS_report_1["Step 1: Check For Receipts, execute SSRS report [TSQL]"]`n```

## Steps

### Step 1: Check For Receipts, execute SSRS report
**Subsystem:** TSQL  

```sql
if (select count (*) from IntegrationStaging.[WMS].[vwPurchaseOrderReceiptsToday]) >  0        Begin       exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name  = 'BC441C47-F11B-458F-A253-50BD0BB9A03E'      End       
```


