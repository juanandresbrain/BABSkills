# dbo.spGiftCard_Extract_Redemptions

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGiftCard_Extract_Redemptions"]
    aw_Giftcards_Redeemed(["aw_Giftcards_Redeemed"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| aw_Giftcards_Redeemed |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spGiftCard_Extract_Redemptions]
-- =============================================================================================================
-- Name: spGiftCard_Extract_Redemptions
--
-- Description:	
--	Pull the giftcard redemptions for pulling the datawarehouse.
--
--
-- Input:		
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Murrish	4/17/2013		Created

-- =============================================================================================================
AS

	SET NOCOUNT ON


	-- Now return all of the records to the process to merge them
	SELECT
		r.transaction_id,
		r.date_key,
		r.Gross_line_Amount AS redemptionAmount,
		r.pos_discount_amount,
		r.reference_no AS giftcardNo,
		r.currency_key,
		r.store_key,
		r.daysSinceLastActivation,
		r.activation_discount_amount,
		r.liftAmount
	FROM
		aw_Giftcards_Redeemed  r WITH (NOLOCK)
	ORDER BY	r.reference_no,
				r.transaction_id
```

