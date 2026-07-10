# Azure.vwWMS_cycleCount_accuracy

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWMS_cycleCount_accuracy"]
    dbo_WMS_cycleCount(["dbo.WMS_cycleCount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WMS_cycleCount |

## View Code

```sql
CREATE view [Azure].[vwWMS_cycleCount_accuracy]

AS
-- =============================================================================================================
--		Name:				Date:			Comments:
--		Ian Wallace			5/18/2021		Initial creation
-- =============================================================================================================



--select * from [dbo].[WMS_cycleCount] where WorkId = 'WK000000924'
 


SELECT [AcceptReject]
      ,[AmtBeforeCount]
      ,cast([ApprovedDate] as date) as 'ApprovedDate'
      ,[ApproverId]
      ,[CostPerUnit]
      ,[CostPrice]
      ,[CounterId]
      ,[dataAreaId]
      ,cast([DateOfCount] as date) as 'DateOfCount'
      ,[FinalCountAmt]
      ,[InventDimId]
      ,[InventJournalNum]
      ,[LicensePlate]
      ,[LineNum]
      ,[Location]
      ,[SKU]
      ,[Tolerance]
      ,[UnitDifference]
	  --, [UnitDifference]*[CostPerUnit] as 'dollarDifference'

	  
	  ,'dollarDifference' = case when ([AmtBeforeCount] = [FinalCountAmt]) then [UnitDifference]*[CostPerUnit]
							else [UnitDifference]*[CostPrice] end

	-- ,[AmtBeforeCount]*[CostPerUnit] as 'perpetualDollarAmt'

	 
	 ,'perpetualDollarAmt' = case when ([AmtBeforeCount] = [FinalCountAmt]) then [AmtBeforeCount]*[CostPerUnit]
							else [AmtBeforeCount]*[CostPrice] end

	   ,'UnitDifferencePerc' = case when AmtBeforeCount = 0 then 1 else ([UnitDifference])/AmtBeforeCount end
      ,'totalUnitAdjustments' = case when [InventJournalNum] like 'INVJ%' then ABS([UnitDifference]) else 0 end

	  ,'dollarAdjustments' = case when [InventJournalNum] like 'INVJ%' then [UnitDifference]*[CostPerUnit] else 0 end

	  --,'unitAccuracy' = case when [InventJournalNum] like 'INVJ%' and AmtBeforeCount = 0 then 1 
			--			  when [InventJournalNum] like 'INVJ%' and AmtBeforeCount <> 0 then 1-ABS([UnitDifference])/AmtBeforeCount	 
			--			else 0 end

	  --,'dollarAccuracy' = case when [InventJournalNum] like 'INVJ%' and AmtBeforeCount = 0 then 1 
			--			  when [InventJournalNum] like 'INVJ%' and AmtBeforeCount <> 0 then 1-ABS(([UnitDifference]*[CostPerUnit]) / [AmtBeforeCount]*[CostPerUnit])
			--			else 0 end
	  ,[Warehouse]
      ,[WorkId]
      ,[WorkStatus]
      ,[InsertDate]
      ,[UpdateDate]
  FROM [dbo].[WMS_cycleCount]
  where [AcceptReject] = 'Accept'
--and WorkId = 'WK000000924'
-- SKU = '028647' and  cast(DateOfCount as date) >= '05/07/2021'
-- SKU = '029093' and  cast(DateOfCount as date) >= '03/25/2021'
-- SKU in ('028647','054964','057580','029116')
--SKU in ('028647','057580','057580','029093','029093','025125','025125')
-- and cast(ApprovedDate as date) > '01/01/1900'
 --and cast(DateOfCount as date) >= '03/01/2021'
```

