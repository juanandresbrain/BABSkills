# dbo.spMergeWebShippingDiscounts

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebShippingDiscounts"]
    dbo_WebShippingDiscounts(["dbo.WebShippingDiscounts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebShippingDiscounts |

## Stored Procedure Code

```sql
create proc spMergeWebShippingDiscounts

as

-------------------------------------------------------------------------
-- spMergeWebItemDiscounts
-- 2017-10-18- Dan Tweedie - Created Proc
-------------------------------------------------------------------------

set nocount on

Merge into dw.dbo.WebShippingDiscounts as target
Using dwstaging.dbo.WebShippingDiscounts as source
On (
			target.ShippingDiscountID = source.ShippingDiscountID
			and
			target.OrderID = source.OrderID
	)
when matched 
	and
		(
			target.PromoCode <> source.PromoCode
			OR
			target.DiscountAmount <> source.DiscountAmount
			OR
			target.DiscountName <> source.DiscountName
		)
		then UPDATE
			set
			target.PromoCode = source.PromoCode,
			target.DiscountAmount = source.DiscountAmount,
			target.DiscountName = source.DiscountName,
			target.UpdateDate = getdate()
When Not Matched By Target 
	Then 
		Insert (
					ShippingDiscountID,
					OrderID,
					PromoCode,
					DiscountAmount,
					DiscountName,
					InsertDate,
					UpdateDate
				)
		Values (	
					source.ShippingDiscountID,
					source.OrderID,
					source.PromoCode,
					source.DiscountAmount,
					source.DiscountName,
					getdate(),
					getdate()
				)
;
```

