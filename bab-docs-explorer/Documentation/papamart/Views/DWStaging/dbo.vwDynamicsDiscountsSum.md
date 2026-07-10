# dbo.vwDynamicsDiscountsSum

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDynamicsDiscountsSum"]
    dbo_vwDiscountFactsReferenceDynamicsStage(["dbo.vwDiscountFactsReferenceDynamicsStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwDiscountFactsReferenceDynamicsStage |

## View Code

```sql
CREATE view [dbo].[vwDynamicsDiscountsSum] as 

with SumTrans as (
select transaction_id,
sum (SumDiscAmount) as SumTransDiscounts, 
sum (SumDiscAmountAbsolute) as SumDiscAmountAbsolute
from [dbo].[vwDiscountFactsReferenceDynamicsStage] df
--where df.transaction_id = '467484542'
group by transaction_id
), 

SumHeader as (

select transaction_id,
sum (SumDiscAmount) as SumTransHeaderDiscounts, 
sum (SumDiscAmountAbsolute) as SumTransHeaderDiscountsAbsolute

from [dbo].[vwDiscountFactsReferenceDynamicsStage] df
where df.DiscountType = 'Header'
--and df.transaction_id = '467484542'
group by transaction_id
),

SumLines as (

select transaction_id,
sum (SumDiscAmount) as SumTransLineDiscounts, 
sum (SumDiscAmountAbsolute) as SumTransLineDiscountsAbsolute

from [dbo].[vwDiscountFactsReferenceDynamicsStage] df
where df.DiscountType = 'Line'
--and df.transaction_id = '467484542'
group by transaction_id

) 

select
st.transaction_id, 
cast(st.SumTransDiscounts as numeric (14,2)) as SumTransDiscounts, 
cast(st.SumDiscAmountAbsolute as numeric (14,2)) as SumTransDiscountsAbsolute, 
cast(isnull(sh.SumTransHeaderDiscounts,0.00) as numeric (14,2)) as SumTransHeaderDiscounts, 
cast(isnull(sh.SumTransHeaderDiscountsAbsolute,0.00) as numeric (14,2)) as SumTransHeaderDiscountsAbsolute, 
cast(isnull(sl.SumTransLineDiscounts,0.00) as numeric (14,2)) as SumTransLineDiscounts,
cast(isnull(sl.SumTransLineDiscountsAbsolute,0.00) as numeric (14,2)) as SumTransLineDiscountsAbsolute
from SumTrans st
left join SumHeader sh on st.transaction_id=sh.transaction_id -- Changed to Left Join on 12/15/22
left join SumLines sl on st.transaction_id=sl.transaction_id  -- Changed to Left Join on 12/15/22
group by st.transaction_id, 
cast(st.SumTransDiscounts as numeric (14,2)), 
cast(st.SumDiscAmountAbsolute as numeric (14,2)), 
cast(isnull(sh.SumTransHeaderDiscounts,0.00) as numeric (14,2)), 
cast(isnull(sh.SumTransHeaderDiscountsAbsolute,0.00) as numeric (14,2)), 
cast(isnull(sl.SumTransLineDiscounts,0.00) as numeric (14,2)),
cast(isnull(sl.SumTransLineDiscountsAbsolute,0.00) as numeric (14,2))
```

