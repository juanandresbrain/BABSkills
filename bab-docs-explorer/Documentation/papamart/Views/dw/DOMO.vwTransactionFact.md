# DOMO.vwTransactionFact

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwTransactionFact"]
    dbo_currency_dim(["dbo.currency_dim"]) --> VIEW
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
    dbo_Transaction_Facts(["dbo.Transaction_Facts"]) --> VIEW
    dbo_Transaction_Type_Dim(["dbo.Transaction_Type_Dim"]) --> VIEW
    DOMO_vwDOMOStores(["DOMO.vwDOMOStores"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.currency_dim |
| dbo.date_dim |
| dbo.time_dim |
| dbo.Transaction_Facts |
| dbo.Transaction_Type_Dim |
| DOMO.vwDOMOStores |

## View Code

```sql
CREATE view [DOMO].[vwTransactionFact]

AS
-- =============================================================================================================
-- Name: [DOMO].[vwTransactionFact]
--
-- Description: Transaction data at the header level.
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Brian Byas			11/11/2015		Initial creation
--		Brian Byas			12/8/2015		Added Correct Party Flag
--		Anthony Delgado		12/17/2015		Added Currency Code
--		Anthony Delgado		04/11/2016		Added merch category buckets; UnitGrossAmount, Units, and Cost
--		Anthony Delgado		06/21/2016		Added StoreTransaction, StoreSalesAmount and FinStoreSalesAmount
--		Anthony Delgado		08/16/2016		Added EnterpriseSellingUnits, GAAPUnits, EnterpriseSellingOnlyFlag, EnterpriseSellingAmount
--		Anthony Delgado		10/05/2016		Added CaptureEligible
--
-- =============================================================================================================
SELECT tff.[transaction_id] AS TransactionID
      ,ds.[StoreID] AS StoreKey
      ,CONVERT(DATE,dd.actual_date) AS TransactionDate
	  ,CAST(CONVERT(VARCHAR,CONVERT(DATE,dd.actual_date)) +' ' + LEFT(CONVERT(TIME,CONVERT(VARCHAR,td.hour) + ':' + CONVERT(VARCHAR,td.minute)),5) + ':00.000' AS DATETIME) AS TransactionDateTime
      ,ttd.[transaction_type] AS TransactionType
      ,tff.[transaction_no] AS TransactionNumber
      ,tff.[register_no] AS RegisterNumber
      ,tff.[GAAP_transaction_flag] AS GAAPTransaction
	  ,tff.[store_transaction_flag] AS StoreTransaction
	  ,tff.[Enterprise_Selling_Only_Flag] AS EnterpriseSellingOnlyTransaction
      ,tff.[donation_only_flag] AS DonationTransaction
      ,tff.[giftcard_only_flag] AS GiftCardOnlyTransaction
	  ,tff.[party_flag] AS PartyFlag
	  ,tff.[total_units] AS TotalUnits
      ,tff.[GAAP_sales_amount] AS GAAPSalesAmount
	  ,tff.[Store_Sales_Amount] AS StoreSalesAmount
	  ,tff.[Enterprise_Selling_Amount] AS EnterpriseSellingAmount
      ,tff.[net_sales_amount] AS NetSalesAmount
	  ,tff.[unit_gross_amount] AS UnitGrossAmount
      ,tff.[unit_net_amount] AS UnitNetAmount
      ,tff.[reward_certificate_amount] AS RewardCertificateAmount
      ,tff.[buy_stuff_amount] AS BuyStuffAmount
	  ,tff.[redemption_amount] AS RedemptionAmount
      ,tff.[tax_amount] AS TaxAmount
	  ,tff.[unit_discount_amount] AS UnitDiscountAmount
      ,tff.[coupon_discount_amount] AS CouponDiscountAmount
      ,tff.[coupon_discount_units] AS CouponDiscountUnits
      ,tff.[giftcard_discount_amount] AS GiftcardDiscountAmount
	  ,tff.[total_discount_amount] AS TotalDiscountAmount
	  ,tff.[receipt_total_amount] AS ReceiptTotalAmount
      ,tff.[fin_GAAP_sales_amount] AS FinGAAPSalesAmount
	  ,tff.[fin_Store_Sales_Amount] AS FinStoreSalesAmount
	  ,tff.[upsell_discount_amount] AS UpsellDiscountAmount
      ,tff.[merchandise_UGA] AS MerchandiseUnitGrossAmount
      ,tff.[merchandise_units] AS MerchandiseUnits
      ,tff.[Gaap_Units] AS GAAPUnits
      ,tff.[Enterprise_Selling_Units] AS EnterpriseSellingUnits
      ,tff.[merchandise_cost] AS MerchandiseCost
      ,tff.[donations_UGA] AS DonationUnitGrossAmount
      ,tff.[donations_units] AS DonationUnits 
      ,tff.[party_deposit_UGA] AS PartyDepositUnitGrossAmount
      ,tff.[party_deposit_units] AS PartyDepositUnits
      ,tff.[giftcard_UGA] AS GiftCardUnitGrossAmount
      ,tff.[giftcard_units] AS GiftCardUnits 
      ,tff.[animal_UGA] AS AnimalUnitGrossAmount
      ,tff.[animal_units] AS AnimalUnits
      ,tff.[animal_cost] AS AnimalCost
      ,tff.[non_animal_UGA] AS NonAnimalUnitGrossAmount
      ,tff.[non_animal_units] AS NonAnimalUnits
      ,tff.[non_animal_cost] AS NonAnimalCost
      ,tff.[footwear_UGA] AS FootwearUnitGrossAmount
      ,tff.[footwear_units] AS FootwearUnits
      ,tff.[footwear_cost] AS FootwearCost
      ,tff.[accessories_UGA] AS AccessoryUnitGrossAmount
      ,tff.[footwear_cost] AS AccessoryCost
      ,tff.[accessories_units] AS AccessoryUnits
      ,tff.[sounds_UGA] AS SoundUnitGrossAmount
      ,tff.[sounds_units] AS SoundUnits
      ,tff.[sounds_cost] AS SoundCost
      ,tff.[clothing_UGA] AS ClothingUnitGrossAmount
      ,tff.[clothing_units] AS ClothingUnits
      ,tff.[clothing_cost] AS ClothingCost
      ,tff.[other_UGA] AS OtherUnitGrossAmount
      ,tff.[other_units] AS OtherUnits
      ,tff.[other_cost] AS OtherCost
      ,tff.[shipping_UGA] AS ShippingUnitGrossAmount
      ,tff.[shipping_units] AS ShippingUnits
      ,tff.[other_fees_UGA] AS OtherFeesUnitGrossAmount
      ,tff.[other_fees_units] AS OtherFeesUnits
      ,tff.[cub_cash_UGA] AS CubCashUnitGrossAmount
      ,tff.[cub_cash_units] AS CubCashUnits
      ,tff.[paid_outs_UGA] AS PaidOutsUnitGrossAmount
      ,tff.[paid_outs_units] AS PaidOutsUnits
      ,tff.[stuffing_supplies_UGA] AS StuffingSuppliesUnitGrossAmount
      ,tff.[stuffing_supplies_units] AS StuffingSuppliesUnits
      ,tff.[sports_UGA] AS SportUnitGrossAmount
      ,tff.[sports_units] AS SportUnits
      ,tff.[sports_cost] AS SportCost
      ,tff.[prestuffed_UGA] AS PresuffedUnitGrossAmount
      ,tff.[prestuffed_units] AS PresuffedUnits
      ,tff.[prestuffed_cost] AS PresuffedCost
      ,tff.[scents_UGA] AS ScentUnitGrossAmount
      ,tff.[scents_units] AS ScentUnits
      ,tff.[scents_cost] AS ScentCost
	  ,cd.currency_code AS CurrencyCode
	  ,CASE WHEN (tff.Store_transaction_flag=1 OR tff.giftcard_only_flag=1) THEN 1 ELSE 0 END AS CaptureEligible,
		tff.EmployeeDiscountUGA,
		tff.ReturnUGA,
		tff.ReturnUnits
  FROM [dw].[dbo].[Transaction_Facts] tff WITH(NOLOCK) INNER JOIN
	    [dw].[DOMO].[vwDOMOStores] ds WITH(NOLOCK)
			ON ds.StoreKey=CONVERT(VARCHAR,tff.store_key) INNER JOIN
		[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON tff.date_key = dd.date_key  INNER JOIN
		[dw].[dbo].[time_dim] td WITH(NOLOCK)
			ON td.time_key = tff.time_key INNER JOIN
		[dw].[dbo].[Transaction_Type_Dim] ttd WITH(NOLOCK)
			ON ttd.transaction_key = tff.transaction_type_key INNER JOIN
		[dw].[dbo].[currency_dim] cd WITH(NOLOCK)
			ON cd.currency_key=tff.currency_key
WHERE dd.actual_date>=DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0))
AND dd.actual_date<CONVERT(DATE,GETDATE())
```

