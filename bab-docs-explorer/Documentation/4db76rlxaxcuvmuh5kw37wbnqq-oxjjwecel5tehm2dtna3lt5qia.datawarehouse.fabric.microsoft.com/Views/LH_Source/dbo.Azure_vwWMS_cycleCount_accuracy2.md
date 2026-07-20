# dbo.Azure_vwWMS_cycleCount_accuracy2

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwWMS_cycleCount_accuracy2"]
    dbo_wms_cyclecount(["dbo.wms_cyclecount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wms_cyclecount |

## View Code

```sql
CREATE VIEW [dbo].[vwWMS_cycleCount_accuracy2]

AS
    SELECT
        sum( [AmtBeforeCount]) AS 'AmtBeforeCount'
      ,cast([DateOfCount] AS DATE) AS 'DateOfCount'
      ,sum([FinalCountAmt]) AS 'FinalCountAmt'
     ,[Location]
      ,[SKU]
      ,sum([UnitDifference]) AS 'UnitDifference'
	,'dollarDifference' = CASE WHEN (sum([AmtBeforeCount]) = sum([FinalCountAmt])) THEN sum([UnitDifference])*max([CostPerUnit])
							ELSE sum([UnitDifference])*max([CostPrice]) END
	 ,'perpetualDollarAmt' = CASE WHEN (sum([AmtBeforeCount]) = sum([FinalCountAmt])) THEN sum([AmtBeforeCount])*max([CostPerUnit])
							ELSE sum([AmtBeforeCount])*max([CostPrice]) END
	 ,'UnitDifferencePerc' = CASE WHEN sum(AmtBeforeCount) = 0 THEN 1 ELSE sum([UnitDifference])/sum(AmtBeforeCount) END
	  ,[Warehouse]
    FROM [LH_Mart].[dbo].[wms_cyclecount]
    --where [AcceptReject] = 'Accept'
    WHERE [AcceptReject] IN ('Accept','None')
    GROUP BY [AcceptReject],[DateOfCount],[SKU],[Location],[Warehouse],[WorkId]
```

