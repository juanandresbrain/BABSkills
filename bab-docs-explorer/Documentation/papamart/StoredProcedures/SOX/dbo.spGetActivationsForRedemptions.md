# dbo.spGetActivationsForRedemptions

**Database:** SOX  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGetActivationsForRedemptions"]
    Staging_BankOfAmerica(["Staging.BankOfAmerica"]) --> SP
    Staging_DWCardBalance(["Staging.DWCardBalance"]) --> SP
    dbo_Giftcards_Activated(["dbo.Giftcards_Activated"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Staging.BankOfAmerica |
| Staging.DWCardBalance |
| dbo.Giftcards_Activated |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: [spGetActivationsForRedemptions]
--
-- Description:	
--		Generate activations for more Redemptions 

--
-- Revision History
--		Name:			Date:			Comments:
--		Brian Byas		8/17/2016		created
-- =============================================================================================================


CREATE PROCEDURE [dbo].[spGetActivationsForRedemptions]
@asOfDateKey int
AS

DECLARE @Source AS varchar(10);
SET @Source = 'VLA' + CAST(@asOfDateKey AS varchar);
--SET @Source = 'VLA' + CAST(@asOfDateKey AS varchar)+'-1';  -- Used This On 4/6/2023 because we had to reprocess Fiscal Year 2022 due to FiServ Incomplete Data


INSERT INTO dw.dbo.Giftcards_Activated
	(	Store_Key,
		transaction_id,
		Date_key,
		activated_amount,
		discount_amount,
		giftcard_no,
		currency_key,
		MID,
		SOURCE)
	SELECT
		-1 AS store_key,
		-1 AS transaction_id,
		b.date_key AS date_key,
		b.balance * -1 AS redemption_amount,
		0 AS discount_amount,
		b.GiftCardNumber AS giftcard_no,
		b.CurrencyKey AS currency_key,
		b.MID AS MID,
		@Source AS [Source]
	FROM
		Staging.DWCardBalance b WITH (NOLOCK)
		LEFT JOIN Staging.BankOfAmerica gb WITH (NOLOCK)
			ON b.GiftCardNumber = gb.CardNumber
	WHERE
		gb.CardNumber IS NULL
		AND b.Balance < 0
```

