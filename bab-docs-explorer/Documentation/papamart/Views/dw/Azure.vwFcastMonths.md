# Azure.vwFcastMonths

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwFcastMonths"]
    Azure_NewDateDim(["Azure.NewDateDim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.NewDateDim |

## View Code

```sql
CREATE view [Azure].[vwFcastMonths]

AS
-- =============================================================================================================
-- Name: [Azure].[vwDateFilter]
-- Description: This view is for the International Sales Forecast report 
-- Dependencies: 
-- Revision History
--		Name:				Date:			Comments:
--		Ian Wallace			8/9/2018		Initial creation
-- =============================================================================================================


WITH 
forecastBaseMonths AS 
	(

select top 12 ROW_NUMBER() OVER (ORDER BY Fiscal_Month_Key) as 'fcastMonth', Fiscal_Month, Fiscal_Month_Key 
from [Azure].[NewDateDim] where Date_Key >= CONVERT(char(10), GetDate()-365,126) 
group by Fiscal_Month,Fiscal_Month_Key 
), 
forecastFutureMonths AS
    (
select top 12 ROW_NUMBER() OVER (ORDER BY Fiscal_Month_Key) as 'fcastMonth', Fiscal_Month, Fiscal_Month_Key 
from [Azure].[NewDateDim] where Date_Key >= CONVERT(char(10), GetDate(),126) 
and datediff(day, getdate(), Date_Key) < 400
group by Fiscal_Month,Fiscal_Month_Key 
)

select b.fcastMonth, b. Fiscal_Month, b.Fiscal_Month_Key, f.fcastMonth as 'fcastMonthOut', f. Fiscal_Month as 'Fiscal_Month_Out', f.Fiscal_Month_Key as 'Fiscal_Month_Key_Out'
from forecastBaseMonths b 
inner join  forecastFutureMonths f on b.fcastMonth = f.fcastMonth
--order by b.fcastMonth asc
```

