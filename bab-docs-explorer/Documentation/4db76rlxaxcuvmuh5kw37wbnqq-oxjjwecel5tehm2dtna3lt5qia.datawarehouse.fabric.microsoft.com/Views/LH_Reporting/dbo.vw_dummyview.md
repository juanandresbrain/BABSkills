# dbo.vw_dummyview

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_dummyview"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIew  vw_dummyview AS
SELECT 
1 As DInt,CAST(2 as Smallint) AS SInt,CAST(3 as BigINT) AS BInt
,CAST(2.021 AS DECIMAL(18,6)) AS decint
, CAST(GETDATE() AS DATETIME2(7)) as ndate
,CAST(123 AS MONEY) as mondata ,CAST(1 AS bit) as bitdata
```

