# dbo.usp_Top20byDepartment

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_Top20byDepartment"]
    dbo_jumpmind_posbydepartment(["dbo.jumpmind_posbydepartment"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_posbydepartment |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[usp_Top20byDepartment]
@StartDate date,
@EndDate date,
@StoreNumber varchar(4)
AS
BEGIN
WITH CTE_Raw AS (
SELECT
    StoreNumber,
    ItemNumber,
    ItemDesc,
    Department,
    DepartmentCode,
    MAX(NetSales) AS NetSales,
    MAX(UnitsSold) AS UnitsSold

    FROM LH_Reporting.dbo.jumpmind_posbydepartment P

    WHERE P.Shcreate_time BETWEEN @StartDate AND @EndDate
    AND P.Slcreate_time BETWEEN @StartDate AND @EndDate
    AND P.StoreNumber = @StoreNumber OR P.StoreNumber = ''
    GROUP BY 
    StoreNumber,
    ItemNumber,
    ItemDesc,
    Department,
    DepartmentCode
),
    CTE_Raw2 AS (
        SELECT 
            StoreNumber,
            ItemNumber,
            ItemDesc,
            Department,
            DepartmentCode,
            NetSales,
            UnitsSold,
            ROW_NUMBER() OVER (PARTITION BY Department ORDER BY NetSales DESC) AS RowNumber
        FROM CTE_Raw
    )
    SELECT
        StoreNumber,
        ItemNumber,
        ItemDesc,
        Department,
        DepartmentCode,
        NetSales,
        UnitsSold,
        RowNumber
    FROM CTE_Raw2 WHERE RowNumber <=20
    ORDER BY Department, NetSales DESC
END
```

