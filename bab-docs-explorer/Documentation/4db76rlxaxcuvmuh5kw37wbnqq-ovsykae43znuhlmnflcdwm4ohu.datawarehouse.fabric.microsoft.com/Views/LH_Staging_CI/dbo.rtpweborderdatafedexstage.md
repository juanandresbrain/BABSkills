# dbo.rtpweborderdatafedexstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.rtpweborderdatafedexstage"]
    dbo_rtpweborderdatafedexstage(["dbo.rtpweborderdatafedexstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.rtpweborderdatafedexstage |

## View Code

```sql
; CREATE   VIEW [dbo].[rtpweborderdatafedexstage] AS SELECT [ShipmentTrackingNumber] COLLATE Latin1_General_CI_AS AS [ShipmentTrackingNumber], [ServiceType] COLLATE Latin1_General_CI_AS AS [ServiceType], [ShipmentDeliveryDate] COLLATE Latin1_General_CI_AS AS [ShipmentDeliveryDate], [NetChargeAmountUSD] COLLATE Latin1_General_CI_AS AS [NetChargeAmountUSD], [Invoicedate] COLLATE Latin1_General_CI_AS AS [Invoicedate], [MasterTrackingNumber] COLLATE Latin1_General_CI_AS AS [MasterTrackingNumber] FROM [dbo].[rtpweborderdatafedexstage]
```

