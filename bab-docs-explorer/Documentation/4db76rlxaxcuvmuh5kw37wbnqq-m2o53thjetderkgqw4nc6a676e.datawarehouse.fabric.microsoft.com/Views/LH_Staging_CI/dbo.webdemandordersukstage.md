# dbo.webdemandordersukstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webdemandordersukstage"]
    dbo_webdemandordersukstage(["dbo.webdemandordersukstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webdemandordersukstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[webdemandordersukstage]
AS
    SELECT [OrderNumber] COLLATE Latin1_General_CI_AS AS [OrderNumber], [OrderDateUTC], [LastUpdateDateUTC], [CustomerID] COLLATE Latin1_General_CI_AS AS [CustomerID], [OrderStatus] COLLATE Latin1_General_CI_AS AS [OrderStatus], [OrderStatusCode] COLLATE Latin1_General_CI_AS AS [OrderStatusCode], [BillingProvince] COLLATE Latin1_General_CI_AS AS [BillingProvince], [BillingPostalCode] COLLATE Latin1_General_CI_AS AS [BillingPostalCode], [BillingCountry] COLLATE Latin1_General_CI_AS AS [BillingCountry], [ShippingProvince] COLLATE Latin1_General_CI_AS AS [ShippingProvince], [ShippingPostalCode] COLLATE Latin1_General_CI_AS AS [ShippingPostalCode], [ShippingCountry] COLLATE Latin1_General_CI_AS AS [ShippingCountry], [SubTotal], [VAT], [VATShipping], [TotalTax], [ShippingTax], [OriginalShipping], [Shipping], [ShippingMethod] COLLATE Latin1_General_CI_AS AS [ShippingMethod], [ShippingMethodCode] COLLATE Latin1_General_CI_AS AS [ShippingMethodCode], [OrderDiscount], [ShippingDiscount], [OrderGrossTotal], [GiftReceipt] COLLATE Latin1_General_CI_AS AS [GiftReceipt], [GiftWrap] COLLATE Latin1_General_CI_AS AS [GiftWrap], [OrderSource] COLLATE Latin1_General_CI_AS AS [OrderSource], [Source1] COLLATE Latin1_General_CI_AS AS [Source1], [Source2] COLLATE Latin1_General_CI_AS AS [Source2], [Source3] COLLATE Latin1_General_CI_AS AS [Source3], [Custom1] COLLATE Latin1_General_CI_AS AS [Custom1], [Custom2] COLLATE Latin1_General_CI_AS AS [Custom2], [Custom3] COLLATE Latin1_General_CI_AS AS [Custom3], [Custom4] COLLATE Latin1_General_CI_AS AS [Custom4], [Custom5] COLLATE Latin1_General_CI_AS AS [Custom5], [CustomOrderAttributes] COLLATE Latin1_General_CI_AS AS [CustomOrderAttributes], [ChannelName] COLLATE Latin1_General_CI_AS AS [ChannelName], [OrderPromotionIDs] COLLATE Latin1_General_CI_AS AS [OrderPromotionIDs], [OrderCampaignIDs] COLLATE Latin1_General_CI_AS AS [OrderCampaignIDs], [OrderCoupons] COLLATE Latin1_General_CI_AS AS [OrderCoupons], [FileName] COLLATE Latin1_General_CI_AS AS [FileName], [SiteCode] COLLATE Latin1_General_CI_AS AS [SiteCode]
    FROM LH_Staging.[dbo].[webdemandordersukstage]
```

