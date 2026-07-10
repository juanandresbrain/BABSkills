# Azure.vwWMS_cycleCount_adjustments

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWMS_cycleCount_adjustments"]
    dbo_WMS_cycleCount(["dbo.WMS_cycleCount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WMS_cycleCount |

## View Code

```sql
CREATE view [Azure].[vwWMS_cycleCount_adjustments]

AS
-- =============================================================================================================
--		Name:				Date:			Comments:
--		Ian Wallace			5/18/2021		Initial creation
-- =============================================================================================================



SELECT 
 cast([DateOfCount] as date) as 'DateOfCount'
,cast([ApprovedDate] as date) as 'ApprovedDate'
,[Location]
,[Warehouse]
,[SKU]
,[CounterId]
,[ApproverId]
,sum([FinalCountAmt]) as 'FinalCountAmt'
,sum([AmtBeforeCount]) as 'AmtBeforeCount'
,sum([UnitDifference]) as 'UnitDifference'
--,sum([CostPrice]) as 'CostPrice'
,sum([UnitDifference]*[CostPrice]) as 'Dollar Difference'
FROM [dbo].[WMS_cycleCount]
where InventJournalNum like 'INVJ%'
--and  SKU in ('056229','015033') and  cast(DateOfCOunt as date) between '02/12/2020' and '02/15/2020'
group by [DateOfCount] ,[ApprovedDate],[Location],[Warehouse],[SKU],[CounterId],[ApproverId]--,[FinalCountAmt],[AmtBeforeCount],[UnitDifference],[CostPrice]

 -- SKU in ('028647','054964','057580','029116')
-- and cast(ApprovedDate as date) > '01/01/1900'
--  and cast(DateOfCount as date) >= '05/01/2021'
```

