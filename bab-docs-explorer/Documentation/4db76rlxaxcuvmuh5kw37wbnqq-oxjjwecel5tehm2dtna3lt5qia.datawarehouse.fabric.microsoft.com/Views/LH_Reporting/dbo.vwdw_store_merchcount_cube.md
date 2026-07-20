# dbo.vwdw_store_merchcount_cube

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_store_merchcount_cube"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_storeopen_dim(["dbo.storeopen_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.storeopen_dim |

## View Code

```sql
CREATE VIEW vwdw_store_merchcount_cube
 AS  
 SELECT  store_key  
   , dd.date_key  
   , MDSE_WGHT AS mdse_wght  
   , cast (1 AS INT) AS numstores  
 FROM  
  LH_Mart.dbo.storeopen_dim AS sod
  INNER JOIN (  
     -- Weekending Dates  
     SELECT date_key  
     FROM  
      LH_Mart.dbo.date_dim AS dd
     WHERE  
      day_of_week = 7
 ) dd  
   ON dd.date_key BETWEEN sod.date_key_from AND sod.date_key_thru
```

