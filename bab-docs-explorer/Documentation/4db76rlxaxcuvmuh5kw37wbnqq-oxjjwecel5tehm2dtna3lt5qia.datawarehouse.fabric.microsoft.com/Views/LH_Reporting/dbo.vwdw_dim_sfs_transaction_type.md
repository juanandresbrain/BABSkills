# dbo.vwdw_dim_sfs_transaction_type

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_dim_sfs_transaction_type"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW vwdw_dim_sfs_transaction_type
AS  
SELECT  
  cast(0 as smallint) AS sfs_transaction_type_key  
  ,'N' AS sfs_transaction_y_n  
  ,'N/A' AS sfs_transaction_new  
  ,'Non-SFS transaction' AS description  
  
UNION ALL  
  
SELECT  
  cast(1 as smallint) AS sfs_transaction_type_key  
  ,'Y' AS sfs_transaction_y_n  
  ,'Y' AS sfs_transaction_new  
  ,'New SFS transaction' AS description  
  
UNION ALL  
  
SELECT  
  cast(2 as smallint) AS sfs_transaction_type_key  
  ,'Y' AS sfs_transaction_y_n  
  ,'N' AS sfs_transaction_new  
  ,'SFS transaction' AS description
```

