# WMS.ModeOfDeliveryWeb

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SHIP_VIA | varchar | 50 | 1 |  |  |  |
| SHIP_VIA_DESC | varchar | 50 | 1 |  |  |  |
| ModeOfDelivery | varchar | 50 | 1 |  |  |  |
| CarrierCode | varchar | 50 | 1 |  |  |  |
| CarrierService | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spReportBearhouseWebStoreInvoiceUpdate](../../StoredProcedures/IntegrationStaging/WMS.spReportBearhouseWebStoreInvoiceUpdate.md)

