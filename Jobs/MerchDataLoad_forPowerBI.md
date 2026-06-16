# Job: MerchDataLoad_forPowerBI

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MerchDataLoad_forPowerBI"]
    JOB --> MerchDataLoad_1["Step 1: MerchDataLoad [SSIS]"]`n    JOB --> Azure_BRF_Products_load_2["Step 2: Azure BRF Products load [TSQL]"]`n    JOB --> Azure_BRF_Store_load_3["Step 3: Azure BRF Store load [TSQL]"]`n```

## Steps

### Step 1: MerchDataLoad
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PowerBILoad\MerchDataLoad.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10040 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Azure BRF Products load
**Subsystem:** TSQL  

```sql
delete from papamart.dw.Azure.ProductsBRF        INSERT INTO papamart.dw.Azure.ProductsBRF             ([ProductKey]             ,[Style]              ,[isBRFstyle])  select [ProductKey],              [Style],               1  from papamart.dw.Azure.vwProducts where [Style] in  (  SELECT    a.style_code  FROM bedrockdb02.ma_01.dbo.style a, bedrockdb02.ma_01.dbo.view_style_attribute_outer b01  WHERE a.style_id =b01.style_id and  b01.attribute_id = 721  and b01.attribute_set_code = 'BRF'   )    
```

### Step 3: Azure BRF Store load
**Subsystem:** TSQL  

```sql
delete from papamart.dw.Azure.StoresBRF        INSERT INTO papamart.dw.Azure.StoresBRF             ([StoreID]             ,[StoreNumber]             ,[StoreKey]              ,[StoreNameAbbr]              ,[isBRFstore])  select [StoreID],   [StoreNumber],   [StoreKey],   [StoreNameAbbr],                  1   from papamart.dw.Azure.vwStores  where StoreNumber in   (    select distinct location_code --, location_name  from bedrockdb02.ma_01.dbo.view_location_attribute_outer v  join bedrockdb02.ma_01.dbo.location l on l.location_id = v.location_id  where v.attribute_set_code = 'BCKFIL'  )  union  select [StoreID],   [StoreNumber],   [StoreKey],   [StoreNameAbbr],                  1   from papamart.dw.Azure.vwStores  where StoreNumber in ('0013','2013')  
```


