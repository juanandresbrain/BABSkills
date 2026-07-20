# dbo.Azure_vwWMS_cycleCount_adjustments

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwWMS_cycleCount_adjustments"]
    dbo_wms_cyclecount(["dbo.wms_cyclecount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wms_cyclecount |

## View Code

```sql
CREATE VIEW [dbo].[vwWMS_cycleCount_adjustments]

AS
    SELECT
    CAST([DateOfCount] AS DATE) AS 'DateOfCount'
,CAST([ApprovedDate] AS DATE) AS 'ApprovedDate'
,[Location]
,[Warehouse]
,[SKU]
,[CounterId]
,[ApproverId]
,SUM([FinalCountAmt]) AS 'FinalCountAmt'
,SUM([AmtBeforeCount]) AS 'AmtBeforeCount'
,SUM([UnitDifference]) AS 'UnitDifference'
,SUM([UnitDifference]*[CostPrice]) AS 'Dollar Difference'
FROM [LH_Mart].[dbo].[wms_cyclecount]
WHERE InventJournalNum LIKE 'INVJ%'
GROUP BY [DateOfCount] ,[ApprovedDate],[Location],[Warehouse],[SKU],[CounterId],[ApproverId]
```

