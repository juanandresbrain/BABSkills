# dbo.vw_InternalTimeCalcs

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_InternalTimeCalcs"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW dbo.vw_InternalTimeCalcs
AS
SELECT        1 AS ID, 'Selected' AS Name
UNION ALL
SELECT        2 AS Expr1, 'YTD' AS Expr2
UNION ALL
SELECT        3 AS Expr1, 'Last 52 Weeks' AS Expr2
UNION ALL
SELECT        4 AS Expr1, 'Last Year YTD' AS Expr2
UNION ALL
SELECT        5 AS Expr1, 'Last Year' AS Expr2
UNION ALL
SELECT        40 AS Expr1, 'Prev Period' AS Expr2
```

