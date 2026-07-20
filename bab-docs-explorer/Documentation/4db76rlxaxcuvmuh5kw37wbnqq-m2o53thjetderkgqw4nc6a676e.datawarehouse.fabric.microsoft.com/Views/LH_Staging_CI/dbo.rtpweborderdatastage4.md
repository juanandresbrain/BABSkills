# dbo.rtpweborderdatastage4

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.rtpweborderdatastage4"]
    dbo_rtpweborderdatastage4(["dbo.rtpweborderdatastage4"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.rtpweborderdatastage4 |

## View Code

```sql
;
CREATE   VIEW [dbo].[rtpweborderdatastage4]
AS
    SELECT [SiteCode] COLLATE Latin1_General_CI_AS AS [SiteCode], [OrderNumber] COLLATE Latin1_General_CI_AS AS [OrderNumber], [CreateDate], [ShipDate], [TotalUnits], [AnimalUnits], [FootwearUnits], [AccessoriesUnits], [SoundUnits], [ClothingUnits], [GiftcardUnits], [SportsUnits], [OtherUnits], [ShipToState] COLLATE Latin1_General_CI_AS AS [ShipToState], [ShipToCountry] COLLATE Latin1_General_CI_AS AS [ShipToCountry], [TrackingNumber] COLLATE Latin1_General_CI_AS AS [TrackingNumber], [GaapSales], [Shipping], [ShipmentTrackingNumber] COLLATE Latin1_General_CI_AS AS [ShipmentTrackingNumber], [ServiceType] COLLATE Latin1_General_CI_AS AS [ServiceType], [ShipmentDeliveryDate] COLLATE Latin1_General_CI_AS AS [ShipmentDeliveryDate], [NetChargeAmountUSD] COLLATE Latin1_General_CI_AS AS [NetChargeAmountUSD], [Invoicedate] COLLATE Latin1_General_CI_AS AS [Invoicedate], [MasterTrackingNumber] COLLATE Latin1_General_CI_AS AS [MasterTrackingNumber]
    FROM LH_Staging.[dbo].[rtpweborderdatastage4]
```

