# azure.vw_wms_cycle_count_accuracy2

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.vw_wms_cycle_count_accuracy2"]
    dbo_wms_cyclecount(["dbo.wms_cyclecount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wms_cyclecount |

## View Code

```sql
CREATE VIEW [azure].[vw_wms_cycle_count_accuracy2]
AS
-- =============================================================================================================
--		Name:				Date:			Comments:
--		Ian Wallace			5/18/2021		Initial creation
-- =============================================================================================================
SELECT SUM([AmtBeforeCount]) AS amt_before_count
	,cast([DateOfCount] AS DATE) AS date_of_count
	,sum([FinalCountAmt]) AS final_count_amt
	,[Location] AS location
	,[SKU] AS sku
	,sum([UnitDifference]) AS unit_difference
	,CASE 
		WHEN (sum([AmtBeforeCount]) = sum([FinalCountAmt]))
			THEN sum([UnitDifference]) * max([CostPerUnit])
		ELSE sum([UnitDifference]) * max([CostPrice])
		END AS dollar_difference
	,CASE 
		WHEN (sum([AmtBeforeCount]) = sum([FinalCountAmt]))
			THEN sum([AmtBeforeCount]) * max([CostPerUnit])
		ELSE sum([AmtBeforeCount]) * max([CostPrice])
		END AS perpetual_dollar_amt
	,CASE 
		WHEN sum(AmtBeforeCount) = 0
			THEN 1
		ELSE sum([UnitDifference]) / sum(AmtBeforeCount)
		END AS unit_difference_perc
	,[Warehouse] AS warehouse
FROM LH_Mart.[dbo].[wms_cyclecount]

WHERE [AcceptReject] IN (
		'Accept'
		,'None'
		)
GROUP BY [AcceptReject]
	,[DateOfCount]
	,[SKU]
	,[Location]
	,[Warehouse]
	,[WorkId]
```

