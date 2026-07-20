# dbo.webshippingfacts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webshippingfacts"]
    dbo_webshippingfacts(["dbo.webshippingfacts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webshippingfacts |

## View Code

```sql
; CREATE   VIEW [dbo].[webshippingfacts] AS     SELECT [CreateDate], [OrderNumber] COLLATE Latin1_General_CI_AS AS [OrderNumber], [ShipToState] COLLATE Latin1_General_CI_AS AS [ShipToState], [ShipToCountry] COLLATE Latin1_General_CI_AS AS [ShipToCountry], [TrackingNumber] COLLATE Latin1_General_CI_AS AS [TrackingNumber], [Shipping], [SiteCode] COLLATE Latin1_General_CI_AS AS [SiteCode], [ShipDate], [ShipmentTrackingNumber] COLLATE Latin1_General_CI_AS AS [ShipmentTrackingNumber], [ServiceType] COLLATE Latin1_General_CI_AS AS [ServiceType], [ShipmentDeliveryDate] COLLATE Latin1_General_CI_AS AS [ShipmentDeliveryDate], [NetChargeAmountUSD] COLLATE Latin1_General_CI_AS AS [NetChargeAmountUSD], [Invoicedate] COLLATE Latin1_General_CI_AS AS [Invoicedate], [MasterTrackingNumber] COLLATE Latin1_General_CI_AS AS [MasterTrackingNumber], [transaction_id], [InsertDate], [UpdateDate]     FROM [dbo].[webshippingfacts]
```

