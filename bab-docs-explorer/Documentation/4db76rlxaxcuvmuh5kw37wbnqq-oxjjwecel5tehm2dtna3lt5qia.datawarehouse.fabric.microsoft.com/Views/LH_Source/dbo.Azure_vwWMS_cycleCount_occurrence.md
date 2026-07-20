# dbo.Azure_vwWMS_cycleCount_occurrence

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwWMS_cycleCount_occurrence"]
    dbo_wms_cyclecount(["dbo.wms_cyclecount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wms_cyclecount |

## View Code

```sql
CREATE VIEW [dbo].[vwWMS_cycleCount_occurrence]

AS

SELECT
    CAST(DateOfCount AS DATE) AS 'Date of the count'
    ,[Location]
    ,Warehouse
    ,WorkId
FROM [LH_Mart].[dbo].[wms_cyclecount]
GROUP BY DateOfCount,[Location],Warehouse, WorkId
```

