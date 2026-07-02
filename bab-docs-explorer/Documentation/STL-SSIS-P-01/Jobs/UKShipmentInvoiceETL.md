# Job: UKShipmentInvoiceETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["UKShipmentInvoiceETL"]
    JOB --> UKShipmentInvoiceETL_1["Step 1: UKShipmentInvoiceETL [SSIS]"]`n    JOB --> Run_Shipment_Invoice_Report_2["Step 2: Run Shipment Invoice Report [TSQL]"]`n    JOB --> Run_UKItemsWithoutUSWeight_SSRS_Report_3["Step 3: Run UKItemsWithoutUSWeight SSRS Report [TSQL]"]`n```

## Steps

### Step 1: UKShipmentInvoiceETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DailyReportingBuild\UKShipmentInvoiceReportETL\UKShipmentInvoiceReportETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10081 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Run Shipment Invoice Report
**Subsystem:** TSQL  

```sql
-- Ireland  if (select count (*)   from Reporting.UKShipmentInvoiceReportStage  where country_code in ('IE')   and datediff(dd, ShipDate, getdate()) = 0) > 0     Begin     exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = 'B1E56F26-1A92-4909-AA27-39E2FDB1C68F'     End    -- Northern Ireland    if (select count (*)   from Reporting.UKShipmentInvoiceReportStage  where ShipTo in ('2052')  and datediff(dd, ShipDate, getdate()) = 0) > 0     Begin     exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = '905B8AD0-27FA-4895-BA2E-020129981C94'     End
```

### Step 3: Run UKItemsWithoutUSWeight SSRS Report
**Subsystem:** TSQL  

```sql
if (select count (*) from wms.vwUKItemsWithoutUSWeightV3) > 0     Begin     exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = '0E5C8D4F-EE64-432E-B615-6384B86C6B5F'    End  
```


