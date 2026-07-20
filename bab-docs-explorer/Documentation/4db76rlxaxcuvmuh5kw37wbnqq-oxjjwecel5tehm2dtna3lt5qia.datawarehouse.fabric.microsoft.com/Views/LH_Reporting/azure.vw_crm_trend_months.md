# azure.vw_crm_trend_months

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.vw_crm_trend_months"]
    dbo_azure_newdatedim(["dbo.azure_newdatedim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_newdatedim |

## View Code

```sql
CREATE view [azure].[vw_crm_trend_months]

AS



WITH 
trendMonths AS 
	(
select top 24 ROW_NUMBER() OVER (ORDER BY Fiscal_Month_Key) as [m_sequence], Fiscal_Month AS fiscal_month, Fiscal_Month_Key AS fiscal_month_key 
from LH_Mart.dbo.azure_newdatedim where Date_Key >= CONVERT(char(10), GetDate()-730,126) 
group by Fiscal_Month,Fiscal_Month_Key 
)

select m.m_sequence, m.fiscal_month, m.fiscal_month_key from trendMonths m
```

