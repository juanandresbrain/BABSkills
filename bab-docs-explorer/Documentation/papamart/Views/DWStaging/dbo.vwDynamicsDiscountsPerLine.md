# dbo.vwDynamicsDiscountsPerLine

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDynamicsDiscountsPerLine"]
    dbo_DiscountFactsReferenceDynamicsStage(["dbo.DiscountFactsReferenceDynamicsStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DiscountFactsReferenceDynamicsStage |

## View Code

```sql
create view [dbo].[vwDynamicsDiscountsPerLine] as 
select transaction_id,
df.line_sequence, 
count (*) as DiscountsPerLine
from [dbo].[DiscountFactsReferenceDynamicsStage] df
--where df.transaction_id = '463372101'
group by transaction_id, 
df.line_sequence
--order by 1 , 2
```

