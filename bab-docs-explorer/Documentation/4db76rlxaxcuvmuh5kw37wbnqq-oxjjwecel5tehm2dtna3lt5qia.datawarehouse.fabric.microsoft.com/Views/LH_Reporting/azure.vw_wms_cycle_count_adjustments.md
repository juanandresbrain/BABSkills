# azure.vw_wms_cycle_count_adjustments

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.vw_wms_cycle_count_adjustments"]
    dbo_wms_cyclecount(["dbo.wms_cyclecount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wms_cyclecount |

## View Code

```sql
CREATE VIEW [azure].[vw_wms_cycle_count_adjustments]
AS
-- =============================================================================================================
--		Name:				Date:			Comments:
--		Ian Wallace			5/18/2021		Initial creation
-- =============================================================================================================
SELECT CAST([DateOfCount] AS DATE) AS date_of_count
	,CAST([ApprovedDate] AS DATE) AS approved_date
	,[Location] AS location
	,[Warehouse] AS warehouse
	,[SKU] AS sku
	,[CounterId] AS counter_id
	,[ApproverId] AS approver_id
	,SUM([FinalCountAmt]) AS final_count_amt
	,SUM([AmtBeforeCount]) AS amt_before_count
	,SUM([UnitDifference]) AS unit_difference
	,sum([UnitDifference] * [CostPrice]) AS dollar_difference
FROM LH_Mart.[dbo].[wms_cyclecount]
WHERE LOWER(InventJournalNum) LIKE 'invj%'
GROUP BY [DateOfCount]
	,[ApprovedDate]
	,[Location]
	,[Warehouse]
	,[SKU]
	,[CounterId]
	,[ApproverId]
```

