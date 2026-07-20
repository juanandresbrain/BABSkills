# dbo.webproductionordersummary

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webproductionordersummary"]
    dbo_webproductionordersummary(["dbo.webproductionordersummary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webproductionordersummary |

## View Code

```sql
;
CREATE   VIEW [dbo].[webproductionordersummary]
AS
    SELECT [ProductionOrderId], [ProductionOrderNumber] COLLATE Latin1_General_CI_AS AS [ProductionOrderNumber], [ProductionOrderSubTotal], [ProductionOrderShippingAndHandling], [ProductionOrderPromoCode] COLLATE Latin1_General_CI_AS AS [ProductionOrderPromoCode], [ProductionOrderPromoDiscount], [ProductionOrderPromoDescription] COLLATE Latin1_General_CI_AS AS [ProductionOrderPromoDescription], [ProductionOrderBearBucksNumber] COLLATE Latin1_General_CI_AS AS [ProductionOrderBearBucksNumber], [ProductionOrderTotal], [ProductionOrderDateTimeCreated], [ProductionOrderDeferredShipDate], [ProductionOrderShippingMethod] COLLATE Latin1_General_CI_AS AS [ProductionOrderShippingMethod], [ProductionOrderTrackingNumber] COLLATE Latin1_General_CI_AS AS [ProductionOrderTrackingNumber], [ProductionOrderBillingStateProvince] COLLATE Latin1_General_CI_AS AS [ProductionOrderBillingStateProvince], [ProductionOrderBillingZipPostalCode] COLLATE Latin1_General_CI_AS AS [ProductionOrderBillingZipPostalCode], [ProductionOrderBillingCountry] COLLATE Latin1_General_CI_AS AS [ProductionOrderBillingCountry], [ProductionOrderShippingStateProvince] COLLATE Latin1_General_CI_AS AS [ProductionOrderShippingStateProvince], [ProductionOrderShippingZipPostalCode] COLLATE Latin1_General_CI_AS AS [ProductionOrderShippingZipPostalCode], [ProductionOrderShippingCountry] COLLATE Latin1_General_CI_AS AS [ProductionOrderShippingCountry], [ProductionOrderIsWillCall], [ProductionOrderIsLoyaltyMember], [ProductionOrderLoyaltyNumber] COLLATE Latin1_General_CI_AS AS [ProductionOrderLoyaltyNumber], [ProductionOrderIsRush], [ProductionOrderWebOrderStatus] COLLATE Latin1_General_CI_AS AS [ProductionOrderWebOrderStatus], [ProductionOrderCatalogName] COLLATE Latin1_General_CI_AS AS [ProductionOrderCatalogName], [ProductionOrderNumberOfPackages], [ProductionOrderWebCartOrderId], [ProductionOrderWebCartUpdateMsgSent], [ProductionOrderSiteCode] COLLATE Latin1_General_CI_AS AS [ProductionOrderSiteCode], [ProductionOrderBearBuilderId] COLLATE Latin1_General_CI_AS AS [ProductionOrderBearBuilderId], [ProductionOrderBuyStuffStamps], [ProductionOrderActuallShippingCost], [ProductionOrderHasShippableProducts], [ProductionOrderWH_version], [ProductionOrderReceiptCode] COLLATE Latin1_General_CI_AS AS [ProductionOrderReceiptCode], [ProductionOrderServerName] COLLATE Latin1_General_CI_AS AS [ProductionOrderServerName], [ProductionOrderStatusID], [StatusDate], [ESReferenceNbr] COLLATE Latin1_General_CI_AS AS [ESReferenceNbr]
    FROM LH_Staging.[dbo].[webproductionordersummary]
```

