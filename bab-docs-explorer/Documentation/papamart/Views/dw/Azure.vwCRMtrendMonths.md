# Azure.vwCRMtrendMonths

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwCRMtrendMonths"]
    Azure_NewDateDim(["Azure.NewDateDim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.NewDateDim |

## View Code

```sql
CREATE view [Azure].[vwCRMtrendMonths]

AS



WITH 
trendMonths AS 
	(
select top 24 ROW_NUMBER() OVER (ORDER BY Fiscal_Month_Key) as 'mSequence', Fiscal_Month, Fiscal_Month_Key 
from [Azure].[NewDateDim] where Date_Key >= CONVERT(char(10), GetDate()-730,126) 
group by Fiscal_Month,Fiscal_Month_Key 
)

select m.mSequence, m. Fiscal_Month, m.Fiscal_Month_Key from trendMonths m
```

