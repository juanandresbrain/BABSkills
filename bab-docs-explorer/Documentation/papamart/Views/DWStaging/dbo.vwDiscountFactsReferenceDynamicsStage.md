# dbo.vwDiscountFactsReferenceDynamicsStage

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDiscountFactsReferenceDynamicsStage"]
    DiscountFactsReferenceDynamicsStage(["DiscountFactsReferenceDynamicsStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| DiscountFactsReferenceDynamicsStage |

## View Code

```sql
CREATE view [dbo].[vwDiscountFactsReferenceDynamicsStage] as 
select 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
case when  s.LineAction in (2,12,15,26)
	 then SumDiscAmount*-1
	 else SumDiscAmount
	 end as SumDiscAmount, 
abs(SumDiscAmount) as SumDiscAmountAbsolute,
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
DiscountType, 
LineAction


	 
from DiscountFactsReferenceDynamicsStage  s
--where s.transaction_id = 467484542
```

