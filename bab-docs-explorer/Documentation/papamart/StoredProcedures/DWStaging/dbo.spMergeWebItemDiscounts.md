# dbo.spMergeWebItemDiscounts

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebItemDiscounts"]
    dbo_WebItemDiscounts(["dbo.WebItemDiscounts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebItemDiscounts |

## Stored Procedure Code

```sql
create proc spMergeWebItemDiscounts

as

-------------------------------------------------------------------------
-- spMergeWebItemDiscounts
-- 2017-10-18- Dan Tweedie - Created Proc
-------------------------------------------------------------------------

set nocount on

Merge into dw.dbo.WebItemDiscounts as target
Using dwstaging.dbo.WebItemDiscounts as source
On (
			target.DiscountID = source.DiscountID
			and
			target.OrderID = source.OrderID
			and 
			target.OrderItemID = source.OrderItemID
	)
when matched 
	and
		(
			target.PromoCode <> source.PromoCode
			OR
			target.DiscountAmount <> source.DiscountAmount
			OR
			target.IsOrderDiscount <> source.IsOrderDiscount
			OR
			target.DiscountName <> source.DiscountName
		)
		then UPDATE
			set
			target.PromoCode = source.PromoCode,
			target.DiscountAmount = source.DiscountAmount,
			target.IsOrderDiscount = source.IsOrderDiscount,
			target.DiscountName = source.DiscountName,
			target.UpdateDate = getdate()
When Not Matched By Target 
	Then 
		Insert (
					DiscountID,
					PromoCode,
					OrderID,
					OrderItemID,
					DiscountAmount,
					IsOrderDiscount,
					DiscountName,
					InsertDate,
					UpdateDate
				)
		Values (	
					source.DiscountID,
					source.PromoCode,
					source.OrderID,
					source.OrderItemID,
					source.DiscountAmount,
					source.IsOrderDiscount,
					source.DiscountName,
					getdate(),
					getdate()
				)
;
```

