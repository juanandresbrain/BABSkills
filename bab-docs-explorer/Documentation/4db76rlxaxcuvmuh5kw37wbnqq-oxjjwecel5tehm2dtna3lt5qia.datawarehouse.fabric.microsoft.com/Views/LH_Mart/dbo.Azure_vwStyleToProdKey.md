# dbo.Azure_vwStyleToProdKey

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwStyleToProdKey"]
    dbo_Azure_vwProducts(["dbo.Azure_vwProducts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Azure_vwProducts |

## View Code

```sql
Create view dbo.Azure_vwStyleToProdKey
as
with Dupes as (select Style,
                 case Left(Style,1)
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
from dbo.Azure_vwProducts
group by Style,case Left(Style,1)
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


 U as (select D.Style,Min(ProductKey) as ProductKey from Dupes D inner join dbo.Azure_vwProducts P on D.Style = P.Style and JCode = JurisdictionCode
group by D.Style),

V as (select d.Style,Min(P.ProductKey) ProductKey from Dupes d inner join dbo.Azure_vwProducts P on d.Style = P.Style
left join U on d.Style = U.Style 
where U.Style is null
group by d.Style),
 
T as (Select * from U union all select * from V)


select P.Style,P.ProductKey from dbo.Azure_vwProducts P
left join Dupes D on P.Style = D.Style
left join T on P.ProductKey = T.ProductKey
where D.Style is null or T.ProductKey is not null
```

