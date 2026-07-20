# dbo.vwdw_turnover_type_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_turnover_type_dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW vwdw_turnover_type_dim		
AS
SELECT 1 AS turnover_type_key, 'U' AS turnover_type_code,'UNCONTROLLED' AS turnover_type_desc
UNION ALL
SELECT 2,'C','CONTROLLED'
```

