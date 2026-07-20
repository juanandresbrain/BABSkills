# dbo.Azure_vwWMS_cycleCount_accuracy

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwWMS_cycleCount_accuracy"]
    dbo_wms_cyclecount(["dbo.wms_cyclecount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.wms_cyclecount |

## View Code

```sql
CREATE VIEW [dbo].[vwWMS_cycleCount_accuracy]

AS
    SELECT [AcceptReject]
      ,[AmtBeforeCount]
      ,cast([ApprovedDate] AS DATE) AS 'ApprovedDate'
      ,[ApproverId]
      ,[CostPerUnit]
      ,[CostPrice]
      ,[CounterId]
      ,[dataAreaId]
      ,cast([DateOfCount] AS DATE) AS 'DateOfCount'
      ,[FinalCountAmt]
      ,[InventDimId]
      ,[InventJournalNum]
      ,[LicensePlate]
      ,[LineNum]
      ,[Location]
      ,[SKU]
      ,[Tolerance]
      ,[UnitDifference]
	  ,'dollarDifference' = CASE WHEN ([AmtBeforeCount] = [FinalCountAmt]) THEN [UnitDifference]*[CostPerUnit]
							ELSE [UnitDifference]*[CostPrice] END
	 ,'perpetualDollarAmt' = CASE WHEN ([AmtBeforeCount] = [FinalCountAmt]) THEN [AmtBeforeCount]*[CostPerUnit]
							ELSE [AmtBeforeCount]*[CostPrice] END

	   ,'UnitDifferencePerc' = CASE WHEN AmtBeforeCount = 0 THEN 1 ELSE ([UnitDifference])/AmtBeforeCount END
      ,'totalUnitAdjustments' = CASE WHEN [InventJournalNum] LIKE 'INVJ%' THEN ABS([UnitDifference]) ELSE 0 END

	  ,'dollarAdjustments' = CASE WHEN [InventJournalNum] LIKE 'INVJ%' THEN [UnitDifference]*[CostPerUnit] ELSE 0 END
	  ,[Warehouse]
      ,[WorkId]
      ,[WorkStatus]
      ,[InsertDate]
      ,[UpdateDate]
    FROM [LH_Mart].[dbo].[wms_cyclecount]
    WHERE [AcceptReject] = 'Accept'
```

