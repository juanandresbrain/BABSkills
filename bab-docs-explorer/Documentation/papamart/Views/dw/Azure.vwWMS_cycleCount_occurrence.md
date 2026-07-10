# Azure.vwWMS_cycleCount_occurrence

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWMS_cycleCount_occurrence"]
    dbo_WMS_cycleCount(["dbo.WMS_cycleCount"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WMS_cycleCount |

## View Code

```sql
CREATE view [Azure].[vwWMS_cycleCount_occurrence]

AS
-- =============================================================================================================
--		Name:				Date:			Comments:
--		Ian Wallace			5/18/2021		Initial creation
-- =============================================================================================================


select 
cast(DateOfCount as date) as 'Date of the count',
Location,
Warehouse,
WorkId
from [dbo].[WMS_cycleCount] 
--where Location = '0216042' and  cast(DateOfCount as date) = '01/25/2021'
group by DateOfCount,Location,Warehouse, WorkId
```

