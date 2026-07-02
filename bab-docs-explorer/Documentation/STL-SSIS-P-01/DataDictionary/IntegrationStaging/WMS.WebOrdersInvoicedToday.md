# WMS.WebOrdersInvoicedToday

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DeckSalesOrderReferenceNumber | varchar | 10 | 1 |  |  |  |
| SHIP_VIA_DESC | varchar | 50 | 1 |  |  |  |
| UTCShipConfirmDateTime | datetime | 8 | 1 |  |  |  |
| OhioShipConfirmDateTime | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spReportBearhouseWebStoreInvoiceUpdate](../../StoredProcedures/IntegrationStaging/WMS.spReportBearhouseWebStoreInvoiceUpdate.md)

