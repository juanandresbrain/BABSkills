# DOMO.vwTransactionFactStoreDaySummaryFranchisee

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwTransactionFactStoreDaySummaryFranchisee"]
    DOMO_vwDOMOStores(["DOMO.vwDOMOStores"]) --> VIEW
    DOMO_vwTransactionFactFranchisee(["DOMO.vwTransactionFactFranchisee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| DOMO.vwDOMOStores |
| DOMO.vwTransactionFactFranchisee |

## View Code

```sql
CREATE view [DOMO].[vwTransactionFactStoreDaySummaryFranchisee]

AS
-- =============================================================================================================
-- Name: [DOMO].[vwTransactionFactStoreDaySummaryFranchisee]
--
-- Description: Transaction summary by store and day for franchisees.
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Anthony Delgado		06/06/2016		Initial creation
--		Anthony Delgado		06/21/2016		Added StoreTransaction, StoreSalesAmount, and FinStoreSalesAmount
--		Anthony Delgado		08/16/2016		Added Enterprise Selling fields
--
-- =============================================================================================================
SELECT
      CONVERT(VARCHAR,ds.StoreID) AS StoreKey
      ,tff.TransactionDate
  	  ,tff.CurrencyCode
      ,SUM(CAST(tff.TotalUnits AS DECIMAL(15, 3))) AS TotalUnits
      ,SUM(CAST(tff.GAAPUnits AS DECIMAL(15, 3))) AS GAAPUnits
      ,SUM(CAST(tff.EnterpriseSellingUnits AS DECIMAL(15, 3))) AS EnterpriseSellingUnits
	  ,SUM(CASE WHEN tff.EnterpriseSellingOnlyTransaction=1 THEN tff.MerchandiseUnits ELSE 0 END) AS EnterpriseSellingOnlyMerchandiseUnits
	  ,SUM(CASE WHEN tff.EnterpriseSellingUnits<>0 THEN tff.MerchandiseUnits ELSE 0 END) AS EnterpriseSellingMerchandiseUnits
      ,SUM(CAST(tff.GAAPSalesAmount AS DECIMAL(15, 3))) AS GAAPSalesAmount
      ,SUM(CAST(tff.StoreSalesAmount AS DECIMAL(15, 3))) AS StoreSalesAmount
	  ,SUM(CAST(tff.EnterpriseSellingAmount AS DECIMAL(15,3))) AS EnterpriseSellingAmount
	  ,SUM(CASE WHEN tff.EnterpriseSellingOnlyTransaction=1 THEN CAST(tff.StoreSalesAmount AS DECIMAL(15,3)) ELSE 0 END) AS EnterpriseSellingOnlyStoreSalesAmount
	  ,SUM(CASE WHEN tff.EnterpriseSellingUnits<>0 THEN CAST(tff.StoreSalesAmount AS DECIMAL(15,3)) ELSE 0 END) AS EnterpriseSellingStoreSalesAmount
      ,SUM(CAST(tff.NetSalesAmount AS DECIMAL(15, 3))) AS NetSalesAmount
      ,SUM(CAST(tff.UnitGrossAmount AS DECIMAL(15, 3))) AS UnitGrossAmount
      ,SUM(CAST(tff.UnitNetAmount AS DECIMAL(15, 3))) AS UnitNetAmount
      ,SUM(CAST(tff.RewardCertificateAmount AS DECIMAL(15, 3))) AS RewardCertificateAmount
      ,SUM(CAST(tff.BuyStuffAmount AS DECIMAL(15, 3))) AS BuyStuffAmount
      ,SUM(CAST(tff.RedemptionAmount AS DECIMAL(15, 3))) AS RedemptionAmount
      ,SUM(CAST(tff.TaxAmount AS DECIMAL(15, 3))) AS TaxAmount
      ,SUM(CAST(tff.UnitDiscountAmount AS DECIMAL(15, 3))) AS UnitDiscountAmount
      ,SUM(CAST(tff.CouponDiscountAmount AS DECIMAL(15, 3))) AS CouponDiscountAmount
      ,SUM(CAST(tff.CouponDiscountUnits AS DECIMAL(15, 3))) AS CouponDiscountUnits
      ,SUM(CAST(tff.GiftcardDiscountAmount AS DECIMAL(15, 3))) AS GiftcardDiscountAmount
      ,SUM(CAST(tff.TotalDiscountAmount AS DECIMAL(15, 3))) AS TotalDiscountAmount
      ,SUM(CAST(tff.ReceiptTotalAmount AS DECIMAL(15, 3))) AS ReceiptTotalAmount
      ,SUM(CAST(tff.FinGAAPSalesAmount AS DECIMAL(15, 3))) AS FinGAAPSalesAmount 
      ,SUM(CAST(tff.FinStoreSalesAmount AS DECIMAL(15, 3))) AS FinStoreSalesAmount 
      ,SUM(CAST(tff.UpsellDiscountAmount AS DECIMAL(15, 3))) AS UpsellDiscountAmount
      ,SUM(CAST(tff.MerchandiseUnitGrossAmount AS DECIMAL(15, 3))) AS MerchandiseUnitGrossAmount
      ,SUM(CAST(tff.MerchandiseUnits AS DECIMAL(15, 3))) AS MerchandiseUnits
      ,SUM(CAST(tff.MerchandiseCost AS DECIMAL(15, 3))) AS MerchandiseCost 
      ,SUM(CAST(tff.DonationUnitGrossAmount AS DECIMAL(15, 3))) AS DonationUnitGrossAmount
      ,SUM(CAST(tff.DonationUnits AS DECIMAL(15, 3))) AS DonationUnits
      ,SUM(CAST(tff.PartyDepositUnitGrossAmount AS DECIMAL(15, 3))) AS PartyDepositUnitGrossAmount
      ,SUM(CAST(tff.PartyDepositUnits AS DECIMAL(15, 3))) AS PartyDepositUnits
      ,SUM(CAST(tff.GiftCardUnitGrossAmount AS DECIMAL(15, 3))) AS GiftCardUnitGrossAmount
      ,SUM(CAST(tff.GiftCardUnits AS DECIMAL(15, 3))) AS GiftCardUnits
      ,SUM(CAST(tff.AnimalUnitGrossAmount AS DECIMAL(15, 3))) AS AnimalUnitGrossAmount
      ,SUM(CAST(tff.AnimalUnits AS DECIMAL(15, 3))) AS AnimalUnits
      ,SUM(CAST(tff.AnimalCost AS DECIMAL(15, 3))) AS AnimalCost
      ,SUM(CAST(tff.NonAnimalUnitGrossAmount AS DECIMAL(15, 3))) AS NonAnimalUnitGrossAmount
      ,SUM(CAST(tff.NonAnimalUnits AS DECIMAL(15, 3))) AS NonAnimalUnits
      ,SUM(CAST(tff.NonAnimalCost AS DECIMAL(15, 3))) AS NonAnimalCost
      ,SUM(CAST(tff.FootwearUnitGrossAmount AS DECIMAL(15, 3))) AS FootwearUnitGrossAmount 
      ,SUM(CAST(tff.FootwearUnits AS DECIMAL(15, 3))) AS FootwearUnits
      ,SUM(CAST(tff.FootwearCost AS DECIMAL(15, 3))) AS FootwearCost
      ,SUM(CAST(tff.AccessoryUnitGrossAmount AS DECIMAL(15, 3))) AS AccessoryUnitGrossAmount
      ,SUM(CAST(tff.AccessoryCost AS DECIMAL(15, 3))) AS AccessoryCost
      ,SUM(CAST(tff.AccessoryUnits AS DECIMAL(15, 3))) AS AccessoryUnits
      ,SUM(CAST(tff.SoundUnitGrossAmount AS DECIMAL(15, 3))) AS SoundUnitGrossAmount
      ,SUM(CAST(tff.SoundUnits AS DECIMAL(15, 3))) AS SoundUnits
      ,SUM(CAST(tff.SoundCost AS DECIMAL(15, 3))) AS SoundCost
      ,SUM(CAST(tff.ClothingUnitGrossAmount AS DECIMAL(15, 3))) AS ClothingUnitGrossAmount
      ,SUM(CAST(tff.ClothingUnits AS DECIMAL(15, 3))) AS ClothingUnits
      ,SUM(CAST(tff.ClothingCost AS DECIMAL(15, 3))) AS ClothingCost
      ,SUM(CAST(tff.OtherUnitGrossAmount AS DECIMAL(15, 3))) AS OtherUnitGrossAmount
      ,SUM(CAST(tff.OtherUnits AS DECIMAL(15, 3))) AS OtherUnits
      ,SUM(CAST(tff.OtherCost AS DECIMAL(15, 3))) AS OtherCost
      ,SUM(CAST(tff.ShippingUnitGrossAmount AS DECIMAL(15, 3))) AS ShippingUnitGrossAmount
      ,SUM(CAST(tff.ShippingUnits AS DECIMAL(15, 3))) AS ShippingUnits
      ,SUM(CAST(tff.OtherFeesUnitGrossAmount AS DECIMAL(15, 3))) AS OtherFeesUnitGrossAmount
      ,SUM(CAST(tff.OtherFeesUnits AS DECIMAL(15, 3))) AS OtherFeesUnits
      ,SUM(CAST(tff.CubCashUnitGrossAmount AS DECIMAL(15, 3))) AS CubCashUnitGrossAmount
      ,SUM(CAST(tff.CubCashUnits AS DECIMAL(15, 3))) AS CubCashUnits
      ,SUM(CAST(tff.PaidOutsUnitGrossAmount AS DECIMAL(15, 3))) AS PaidOutsUnitGrossAmount
      ,SUM(CAST(tff.PaidOutsUnits AS DECIMAL(15, 3))) AS PaidOutsUnits
      ,SUM(CAST(tff.StuffingSuppliesUnitGrossAmount AS DECIMAL(15, 3))) AS StuffingSuppliesUnitGrossAmount
      ,SUM(CAST(tff.StuffingSuppliesUnits AS DECIMAL(15, 3))) AS StuffingSuppliesUnits
      ,SUM(CAST(tff.SportUnitGrossAmount AS DECIMAL(15, 3))) AS SportUnitGrossAmount
      ,SUM(CAST(tff.SportUnits AS DECIMAL(15, 3))) AS SportUnits
      ,SUM(CAST(tff.SportCost AS DECIMAL(15, 3))) AS SportCost
      ,SUM(CAST(tff.PresuffedUnitGrossAmount AS DECIMAL(15, 3))) AS PresuffedUnitGrossAmount
      ,SUM(CAST(tff.PresuffedUnits AS DECIMAL(15, 3))) AS PresuffedUnits
      ,SUM(CAST(tff.PresuffedCost AS DECIMAL(15, 3))) AS PresuffedCost
      ,SUM(CAST(tff.ScentUnitGrossAmount AS DECIMAL(15, 3))) AS ScentUnitGrossAmount
      ,SUM(CAST(tff.ScentUnits AS DECIMAL(15, 3))) AS ScentUnits
      ,SUM(CAST(tff.ScentCost AS DECIMAL(15, 3))) AS ScentCost
	  ,COUNT(DISTINCT tff.TransactionID) AS TransactionCount
	  ,SUM(tff.GAAPTransaction) AS GAAPTransactionCount
	  ,SUM(tff.StoreTransaction) AS StoreTransactionCount
	  ,SUM(CASE WHEN tff.EnterpriseSellingUnits<>0 THEN 1 ELSE 0 END) AS EnterpriseSellingTransactionCount
	  ,SUM(tff.EnterpriseSellingOnlyTransaction) AS EnterpriseSellingOnlyTransactionCount
	  ,SUM(tff.PartyFlag) AS PartyCount
	  ,SUM(CASE WHEN tff.partyflag=1 THEN GAAPSalesAmount ELSE 0 END) AS PartyGAAPSalesAmount
	  ,SUM(CASE WHEN tff.partyflag=1 THEN TotalUnits ELSE 0 END) AS PartyUnits
	  ,SUM(tff.CaptureEligible) AS CaptureEligible,
	  SUM(CAST(ISNULL(tff.EmployeeDiscountUGA,0) AS DECIMAL(15,3))) AS EmployeeDiscountUGA,
		SUM(CAST(ISNULL(tff.ReturnUGA,0) AS DECIMAL(15,3))) AS ReturnUGA,
		SUM(CAST(ISNULL(tff.ReturnUnits,0) AS int)) AS ReturnUnits,
		0 as PostVoidUGA,
		0 as PostVoidUnits
FROM dw.DOMO.vwTransactionFactFranchisee tff
INNER JOIN [dw].[DOMO].[vwDOMOStores] ds
	ON CAST(ds.StoreID AS VARCHAR(6))=CAST(tff.StoreKey AS VARCHAR(6))
WHERE LEFT(ds.TradingGroup,9) = 'Franchise'
--ds.TradingGroup IN ('Franchise - BAB GULF FZE','Franchise - BABW-AU','Franchise - Build A Bear Deutschland GmbH','Franchise - INTENCITY ENTERTAINMENT (PTY) LTD')

GROUP BY 
	CONVERT(VARCHAR,ds.StoreID),
    tff.TransactionDate,
    tff.CurrencyCode
```

