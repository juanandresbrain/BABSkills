# Azure.vwStyleToProdKey

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwStyleToProdKey"]
    azure_vwProducts(["azure.vwProducts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| azure.vwProducts |

## View Code

```sql
Create view [Azure].[vwStyleToProdKey]

as
-- =============================================================================================================
-- Name: [Azure].[vwStyleToProdKey]
--
-- Description: Product Dimension
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		John Eck			12/27/2018		Initial Creation

--											
-- =============================================================================================================



with Dupes as (select Style,
                 case Left(style,1)
				 When 0 then 'US'
				 When 1 then 'US'
				 When 2 then 'US'
				 When 3 then 'US'
				 When 4 then 'UK'
				 When 5 then 'UK'
				 When 6 then 'UK'
				 When 7 then 'UK'
				 When 7 then 'UK'
				 ELSE 'CN' END as JCode
from azure.vwProducts 
group by style,case Left(style,1)
				 When 0 then 'US'
				 When 1 then 'US'
				 When 2 then 'US'
				 When 3 then 'US'
				 When 4 then 'UK'
				 When 5 then 'UK'
				 When 6 then 'UK'
				 When 7 then 'UK'
				 When 7 then 'UK'
				 ELSE 'CN' END
having count(1) > 1),


 U as (select D.Style,Min(productkey) as ProductKey from dupes D inner join azure.vwProducts P on d.style = p.style and jCode = JurisdictionCode
group by D.Style),

V as (select D.Style,Min(P.productkey) productKey from dupes d inner join azure.vwProducts P on d.style = p.style
left join U on d.style = U.style 
where u.style is null
group by D.Style),
 
T as (Select * from U union all select * from v)


select p.style,p.ProductKey from azure.vwProducts P
left join Dupes D on p.Style = d.style
left join T on P.ProductKey = T.productKey
where D.Style is null or t.ProductKey is not null
```

