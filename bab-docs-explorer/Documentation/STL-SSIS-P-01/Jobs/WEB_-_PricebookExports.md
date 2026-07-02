# Job: WEB - PricebookExports

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PricebookExports"]
    JOB --> SSIS___WebPricebook_1["Step 1: SSIS - WebPricebook [SSIS]"]`n    JOB --> SSIS___PimBundleSkuExtract___Package_Target__Promo_2["Step 2: SSIS - PimBundleSkuExtract - Package Target: Promo [SSIS]"]`n    JOB --> JobCompletionNotice_3["Step 3: JobCompletionNotice [TSQL]"]`n    JOB --> Run_PricebookExceptionReport_4["Step 4: Run PricebookExceptionReport [TSQL]"]`n```

## Steps

### Step 1: SSIS - WebPricebook
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebPricebook\WebPricebook.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10151 /Par PricebookRunDate;"\" NULL\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: SSIS - PimBundleSkuExtract - Package Target: Promo
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PimBundleSkuExtract\PimBundleSkuExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10179 /Par PackageTarget;Promo /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: JobCompletionNotice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Web Pricebooks Export',   @SQLAgent = 'WebPricebookExports',  @Recipients = 'biadmin@buildabear.com'
```

### Step 4: Run PricebookExceptionReport
**Subsystem:** TSQL  

```sql
if     (   select count (*)   from bedrockdb02.me_01.dbo.vwWebProductPrice p   left join bedrockdb02.me_01.dbo.vwWebProductPriceIB i on p.style_code=i.style_code         and p.Catalog=i.Catalog   left join bedrockdb02.me_01.dbo.style s (nolock)  on s.style_code=p.style_code   left join papamart.dw.dbo.WebInventoryRollups dw on dw.stylecode=p.style_code   where isnull(p.SalePrice,0) <> isnull(i.IbSalePrice,0)  ) > 0 --Are There any exceptions?   and convert(varchar, getdate(), 108) >= '11:30:00' -- After 11:30 am run  and convert(varchar, getdate(), 108) <= '16:59:00' -- Before 5pm or 1130 pm   and datepart(dw,getdate()) = 4 -- 4 = Wednesday Only     --select datepart(dw,getdate())    Begin     --Print 'Success!!!'  exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = '2716D57C-C300-4966-B9D5-4A9BFF97727A'    End    
```


