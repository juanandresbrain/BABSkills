# dbo.webshippingfacts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
;

CREATE VIEW dbo.webshippingfacts AS SELECT CreateDate, OrderNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS OrderNumber, ShipToState COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipToState, ShipToCountry COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipToCountry, TrackingNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS TrackingNumber, Shipping, SiteCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS SiteCode, ShipDate, ShipmentTrackingNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipmentTrackingNumber, ServiceType COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ServiceType, ShipmentDeliveryDate COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipmentDeliveryDate, NetChargeAmountUSD COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS NetChargeAmountUSD, Invoicedate COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Invoicedate, MasterTrackingNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS MasterTrackingNumber, transaction_id, InsertDate, UpdateDate FROM LH_Mart.dbo.webshippingfacts;;
```

