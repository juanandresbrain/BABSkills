# dbo.vwBI_TransactionFactSummary

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBI_TransactionFactSummary"]
    dbo_currency_dim(["dbo.currency_dim"]) --> VIEW
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
    dbo_Transaction_Facts(["dbo.Transaction_Facts"]) --> VIEW
    dbo_Transaction_Type_Dim(["dbo.Transaction_Type_Dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.currency_dim |
| dbo.date_dim |
| dbo.time_dim |
| dbo.Transaction_Facts |
| dbo.Transaction_Type_Dim |

## View Code

```sql
CREATE view [dbo].[vwBI_TransactionFactSummary]

AS

with TransactionFacts as
(
		SELECT tff.[transaction_id] AS TransactionID
			  ,tff.store_key as StoreKey
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
				[dw].[dbo].[date_dim] dd WITH(NOLOCK)
					ON tff.date_key = dd.date_key  INNER JOIN
				[dw].[dbo].[time_dim] td WITH(NOLOCK)
					ON td.time_key = tff.time_key INNER JOIN
				[dw].[dbo].[Transaction_Type_Dim] ttd WITH(NOLOCK)
					ON ttd.transaction_key = tff.transaction_type_key INNER JOIN
				[dw].[dbo].[currency_dim] cd WITH(NOLOCK)
					ON cd.currency_key=tff.currency_key
		--WHERE dd.actual_date>=DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0))
		--AND dd.actual_date<CONVERT(DATE,GETDATE())
		where dd.fiscal_year in (2017,2018)
)

SELECT 
		tf.StoreKey
		,tf.TransactionDate
  		,tf.CurrencyCode
		,SUM(CAST(tf.TotalUnits AS DECIMAL(15, 3))) AS TotalUnits
		,SUM(CAST(tf.GAAPUnits AS DECIMAL(15, 3))) AS GAAPUnits
		,SUM(CAST(tf.EnterpriseSellingUnits AS DECIMAL(15, 3))) AS EnterpriseSellingUnits
		,SUM(CASE WHEN tf.EnterpriseSellingOnlyTransaction=1 THEN tf.MerchandiseUnits ELSE 0 END) AS EnterpriseSellingOnlyMerchandiseUnits
		,SUM(CASE WHEN tf.EnterpriseSellingUnits<>0 THEN tf.MerchandiseUnits ELSE 0 END) AS EnterpriseSellingMerchandiseUnits
		,SUM(CAST(tf.GAAPSalesAmount AS DECIMAL(15, 3))) AS GAAPSalesAmount
		,SUM(CAST(tf.StoreSalesAmount AS DECIMAL(15, 3))) AS StoreSalesAmount
		,SUM(CAST(tf.EnterpriseSellingAmount AS DECIMAL(15,3))) AS EnterpriseSellingAmount
		,SUM(CASE WHEN tf.EnterpriseSellingOnlyTransaction=1 THEN CAST(tf.StoreSalesAmount AS DECIMAL(15,3)) ELSE 0 END) AS EnterpriseSellingOnlyStoreSalesAmount
		,SUM(CASE WHEN tf.EnterpriseSellingUnits<>0 THEN CAST(tf.StoreSalesAmount AS DECIMAL(15,3)) ELSE 0 END) AS EnterpriseSellingStoreSalesAmount
		,SUM(CAST(tf.NetSalesAmount AS DECIMAL(15, 3))) AS NetSalesAmount
		,SUM(CAST(tf.UnitGrossAmount AS DECIMAL(15, 3))) AS UnitGrossAmount
		,SUM(CAST(tf.UnitNetAmount AS DECIMAL(15, 3))) AS UnitNetAmount
		,SUM(CAST(tf.RewardCertificateAmount AS DECIMAL(15, 3))) AS RewardCertificateAmount
		,SUM(CAST(tf.BuyStuffAmount AS DECIMAL(15, 3))) AS BuyStuffAmount
		,SUM(CAST(tf.RedemptionAmount AS DECIMAL(15, 3))) AS RedemptionAmount
		,SUM(CAST(tf.TaxAmount AS DECIMAL(15, 3))) AS TaxAmount
		,SUM(CAST(tf.UnitDiscountAmount AS DECIMAL(15, 3))) AS UnitDiscountAmount
		,SUM(CAST(tf.CouponDiscountAmount AS DECIMAL(15, 3))) AS CouponDiscountAmount
		,SUM(CAST(tf.CouponDiscountUnits AS DECIMAL(15, 3))) AS CouponDiscountUnits
		,SUM(CAST(tf.GiftcardDiscountAmount AS DECIMAL(15, 3))) AS GiftcardDiscountAmount
		,SUM(CAST(tf.TotalDiscountAmount AS DECIMAL(15, 3))) AS TotalDiscountAmount
		,SUM(CAST(tf.ReceiptTotalAmount AS DECIMAL(15, 3))) AS ReceiptTotalAmount
		,SUM(CAST(tf.FinGAAPSalesAmount AS DECIMAL(15, 3))) AS FinGAAPSalesAmount 
		,SUM(CAST(tf.FinStoreSalesAmount AS DECIMAL(15,3))) AS FinStoreSalesAmount
		,SUM(CAST(tf.UpsellDiscountAmount AS DECIMAL(15, 3))) AS UpsellDiscountAmount
		,SUM(CAST(tf.MerchandiseUnitGrossAmount AS DECIMAL(15, 3))) AS MerchandiseUnitGrossAmount
		,SUM(CAST(tf.MerchandiseUnits AS DECIMAL(15, 3))) AS MerchandiseUnits
		,SUM(CAST(tf.MerchandiseCost AS DECIMAL(15, 3))) AS MerchandiseCost 
		,SUM(CAST(tf.DonationUnitGrossAmount AS DECIMAL(15, 3))) AS DonationUnitGrossAmount
		,SUM(CAST(tf.DonationUnits AS DECIMAL(15, 3))) AS DonationUnits
		,SUM(CAST(tf.PartyDepositUnitGrossAmount AS DECIMAL(15, 3))) AS PartyDepositUnitGrossAmount
		,SUM(CAST(tf.PartyDepositUnits AS DECIMAL(15, 3))) AS PartyDepositUnits
		,SUM(CAST(tf.GiftCardUnitGrossAmount AS DECIMAL(15, 3))) AS GiftCardUnitGrossAmount
		,SUM(CAST(tf.GiftCardUnits AS DECIMAL(15, 3))) AS GiftCardUnits
		,SUM(CAST(tf.AnimalUnitGrossAmount AS DECIMAL(15, 3))) AS AnimalUnitGrossAmount
		,SUM(CAST(tf.AnimalUnits AS DECIMAL(15, 3))) AS AnimalUnits
		,SUM(CAST(tf.AnimalCost AS DECIMAL(15, 3))) AS AnimalCost
		,SUM(CAST(tf.NonAnimalUnitGrossAmount AS DECIMAL(15, 3))) AS NonAnimalUnitGrossAmount
		,SUM(CAST(tf.NonAnimalUnits AS DECIMAL(15, 3))) AS NonAnimalUnits
		,SUM(CAST(tf.NonAnimalCost AS DECIMAL(15, 3))) AS NonAnimalCost
		,SUM(CAST(tf.FootwearUnitGrossAmount AS DECIMAL(15, 3))) AS FootwearUnitGrossAmount 
		,SUM(CAST(tf.FootwearUnits AS DECIMAL(15, 3))) AS FootwearUnits
		,SUM(CAST(tf.FootwearCost AS DECIMAL(15, 3))) AS FootwearCost
		,SUM(CAST(tf.AccessoryUnitGrossAmount AS DECIMAL(15, 3))) AS AccessoryUnitGrossAmount
		,SUM(CAST(tf.AccessoryCost AS DECIMAL(15, 3))) AS AccessoryCost
		,SUM(CAST(tf.AccessoryUnits AS DECIMAL(15, 3))) AS AccessoryUnits
		,SUM(CAST(tf.SoundUnitGrossAmount AS DECIMAL(15, 3))) AS SoundUnitGrossAmount
		,SUM(CAST(tf.SoundUnits AS DECIMAL(15, 3))) AS SoundUnits
		,SUM(CAST(tf.SoundCost AS DECIMAL(15, 3))) AS SoundCost
		,SUM(CAST(tf.ClothingUnitGrossAmount AS DECIMAL(15, 3))) AS ClothingUnitGrossAmount
		,SUM(CAST(tf.ClothingUnits AS DECIMAL(15, 3))) AS ClothingUnits
		,SUM(CAST(tf.ClothingCost AS DECIMAL(15, 3))) AS ClothingCost
		,SUM(CAST(tf.OtherUnitGrossAmount AS DECIMAL(15, 3))) AS OtherUnitGrossAmount
		,SUM(CAST(tf.OtherUnits AS DECIMAL(15, 3))) AS OtherUnits
		,SUM(CAST(tf.OtherCost AS DECIMAL(15, 3))) AS OtherCost
		,SUM(CAST(tf.ShippingUnitGrossAmount AS DECIMAL(15, 3))) AS ShippingUnitGrossAmount
		,SUM(CAST(tf.ShippingUnits AS DECIMAL(15, 3))) AS ShippingUnits
		,SUM(CAST(tf.OtherFeesUnitGrossAmount AS DECIMAL(15, 3))) AS OtherFeesUnitGrossAmount
		,SUM(CAST(tf.OtherFeesUnits AS DECIMAL(15, 3))) AS OtherFeesUnits
		,SUM(CAST(tf.CubCashUnitGrossAmount AS DECIMAL(15, 3))) AS CubCashUnitGrossAmount
		,SUM(CAST(tf.CubCashUnits AS DECIMAL(15, 3))) AS CubCashUnits
		,SUM(CAST(tf.PaidOutsUnitGrossAmount AS DECIMAL(15, 3))) AS PaidOutsUnitGrossAmount
		,SUM(CAST(tf.PaidOutsUnits AS DECIMAL(15, 3))) AS PaidOutsUnits
		,SUM(CAST(tf.StuffingSuppliesUnitGrossAmount AS DECIMAL(15, 3))) AS StuffingSuppliesUnitGrossAmount
		,SUM(CAST(tf.StuffingSuppliesUnits AS DECIMAL(15, 3))) AS StuffingSuppliesUnits
		,SUM(CAST(tf.SportUnitGrossAmount AS DECIMAL(15, 3))) AS SportUnitGrossAmount
		,SUM(CAST(tf.SportUnits AS DECIMAL(15, 3))) AS SportUnits
		,SUM(CAST(tf.SportCost AS DECIMAL(15, 3))) AS SportCost
		,SUM(CAST(tf.PresuffedUnitGrossAmount AS DECIMAL(15, 3))) AS PresuffedUnitGrossAmount
		,SUM(CAST(tf.PresuffedUnits AS DECIMAL(15, 3))) AS PresuffedUnits
		,SUM(CAST(tf.PresuffedCost AS DECIMAL(15, 3))) AS PresuffedCost
		,SUM(CAST(tf.ScentUnitGrossAmount AS DECIMAL(15, 3))) AS ScentUnitGrossAmount
		,SUM(CAST(tf.ScentUnits AS DECIMAL(15, 3))) AS ScentUnits
		,SUM(CAST(tf.ScentCost AS DECIMAL(15, 3))) AS ScentCost
		,COUNT(DISTINCT tf.TransactionID) AS TransactionCount
		,SUM(tf.GAAPTransaction) AS GAAPTransactionCount
		,SUM(tf.StoreTransaction) AS StoreTransactionCount
		,SUM(CASE WHEN tf.EnterpriseSellingAmount<>0 THEN 1 ELSE 0 END) AS EnterpriseSellingTransactionCount
		,SUM(tf.EnterpriseSellingOnlyTransaction) AS EnterpriseSellingOnlyTransactionCount
		,SUM(tf.PartyFlag) AS PartyCount
		,SUM(CASE WHEN tf.partyflag=1 THEN tf.GAAPSalesAmount ELSE 0 END) AS PartyGAAPSalesAmount
		,SUM(CASE WHEN tf.partyflag=1 THEN tf.TotalUnits ELSE 0 END) AS PartyUnits
		,SUM(tf.CaptureEligible) AS CaptureEligibleTransactionCount,
		SUM(CAST(ISNULL(tf.EmployeeDiscountUGA,0) AS DECIMAL(15,3))) AS EmployeeDiscountUGA,
		SUM(CAST(ISNULL(tf.ReturnUGA,0) AS DECIMAL(15,3))) AS ReturnUGA,
		SUM(CAST(ISNULL(tf.ReturnUnits,0) AS int)) AS ReturnUnits
FROM TransactionFacts tf
where datepart(yyyy, tf.TransactionDate) in (2017, 2018)

GROUP BY 
	tf.StoreKey,
	tf.TransactionDate,
	tf.CurrencyCode
```

