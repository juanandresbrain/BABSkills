# Job: WMS_EmailDistributionsCreatedToday

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_EmailDistributionsCreatedToday"]
    JOB --> WMS_EmailDistributionsCreatedToday_1["Step 1: WMS_EmailDistributionsCreatedToday [SSIS]"]`n    JOB --> Run_SSRS_Report___WMS_DistributionsExportedEstimatedCartons_2["Step 2: Run SSRS Report - WMS_DistributionsExportedEstimatedCartons [TSQL]"]`n```

## Steps

### Step 1: WMS_EmailDistributionsCreatedToday
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_EmailDistributionsCreatedToday\WMS_EmailDistributionsCreatedToday.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10101 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Run SSRS Report - WMS_DistributionsExportedEstimatedCartons
**Subsystem:** TSQL  

```sql
If (    (     select count (*) as MerchDistros     from bedrockdb02.me_01.dbo.distribution_data_after_split ddas (nolock)     join bedrockdb02.me_01.dbo.location l (nolock) on l.location_code = ddas.destid     join bedrockdb02.me_01.dbo.jurisdiction j (nolock) on j.jurisdiction_id = l.jurisdiction_id     where ddas.released = '1'     and j.jurisdiction_code in ('HOME', 'CA')     and datediff(dd, ddas.release_date, getdate()) = 0     and (ddas.destid < '1000' and ddas.destid not in ('0013', '0960', '0975'))     and ddas.rec_type in ('1','3','7')     and ddas.SourceID = '0980' --Added as we only pull 9980 from Dynamics for supplies.     )   > 0       or     (     select count (*)     from bedrockdb02.me_01.dbo.tmpSupplyOrdersStaged  S     left JOIN [stl-ssis-p-01].IntegrationStaging.[WMS].[ItemsUOM] u on  U.ProductNumber = S.ItemNumber     where U.Entity = '1100'     and U.FromUnitSymbol in ('CS') -- As of 3/2/2021 Santiago did not want to include Bales in the report, only Cases\Cartons     and u.ToUnitSymbol = 'EA'     and datediff(dd, s.OrderDate, getdate()) = 0    )   > 0    )  and convert(varchar, getdate(), 108) < '19:30:00' -- Only Run at 615 run of job    Begin     --Print 'Hello'  exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name ='EF002AB4-4207-47B7-9962-9C482133CC77'    End   
```


