# dbo.vwDiscountFactsReferenceDynamicsHeader

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDiscountFactsReferenceDynamicsHeader"]
    DiscountFactsReferenceDynamicsStage(["DiscountFactsReferenceDynamicsStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| DiscountFactsReferenceDynamicsStage |

## View Code

```sql
CREATE view [dbo].[vwDiscountFactsReferenceDynamicsHeader]
as 

select 
d.transaction_date, 
d.transaction_id, 
d.line_id, 
d.line_sequence, 
sum(d.SumDiscAmount) as SumDiscAmount, 
--d.line_object, 
--d.line_object_description, 
--d.line_object_type, 
--d.object_type_display_descr, 
d.DiscountType, 
d.LineAction


from DiscountFactsReferenceDynamicsStage d (nolock)
--where d.transaction_id = '467543204'
group by d.transaction_date, 
d.transaction_id, 
d.line_id, 
d.line_sequence, 
--d.SumDiscAmount, 
--d.line_object, 
--d.line_object_description, 
--d.line_object_type, 
--d.object_type_display_descr, 
d.DiscountType, 
d.LineAction
```

