# dbo.vwDynamicsDiscountsSum_Bak20230330

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDynamicsDiscountsSum_Bak20230330"]
    dbo_DiscountFactsReferenceDynamicsStage(["dbo.DiscountFactsReferenceDynamicsStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DiscountFactsReferenceDynamicsStage |

## View Code

```sql
CREATE view [dbo].[vwDynamicsDiscountsSum_Bak20230330] as 

with SumTrans as (
select transaction_id,
sum (SumDiscAmount) as SumTransDiscounts
from [dbo].[DiscountFactsReferenceDynamicsStage] df
--where df.transaction_id = '463372101'
group by transaction_id
), 

SumHeader as (

select transaction_id,
sum (SumDiscAmount) as SumTransHeaderDiscounts

from [dbo].[DiscountFactsReferenceDynamicsStage] df
where df.DiscountType = 'Header'
--and df.transaction_id = '463372101'
group by transaction_id
),

SumLines as (

select transaction_id,
sum (SumDiscAmount) as SumTransLineDiscounts

from [dbo].[DiscountFactsReferenceDynamicsStage] df
where df.DiscountType = 'Line'
--and df.transaction_id = '463372101'
group by transaction_id

) 

select
st.transaction_id, 
cast(st.SumTransDiscounts as numeric (14,2)) as SumTransDiscounts, 
cast(isnull(sh.SumTransHeaderDiscounts,0.00) as numeric (14,2)) as SumTransHeaderDiscounts, 
cast(isnull(sl.SumTransLineDiscounts,0.00) as numeric (14,2)) as SumTransLineDiscounts
from SumTrans st
left join SumHeader sh on st.transaction_id=sh.transaction_id -- Changed to Left Join on 12/15/22
left join SumLines sl on st.transaction_id=sl.transaction_id  -- Changed to Left Join on 12/15/22
group by st.transaction_id, 
cast(st.SumTransDiscounts as numeric (14,2)), 
cast(isnull(sh.SumTransHeaderDiscounts,0.00) as numeric (14,2)), 
cast(isnull(sl.SumTransLineDiscounts,0.00) as numeric (14,2))
```

