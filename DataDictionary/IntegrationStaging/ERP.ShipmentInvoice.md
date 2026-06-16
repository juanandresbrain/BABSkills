# ERP.ShipmentInvoice

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DlvMode | varchar | 50 | 1 |  |  |  |
| InventLocationId | varchar | 10 | 1 |  |  |  |
| ItemId | varchar | 7 | 1 |  |  |  |
| OrderRef | varchar | 20 | 1 |  |  |  |
| Qty | numeric | 17 | 1 |  |  |  |
| WhseUnitQty | int | 4 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ShipTo | varchar | 10 | 1 |  |  |  |
| CartonNumber | varchar | 20 | 1 |  |  |  |
| PalletID | varchar | 52 | 1 |  |  |  |
| RecType | varchar | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| Transmitted | int | 4 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| BatchID | nvarchar | 104 | 1 |  |  |  |
| UDALocation | varchar | 10 | 1 |  |  |  |
| Warehouse | varchar | 10 | 1 |  |  |  |
| SalesOrderLineNumber | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spOutputShipmentInvoice_TransferXMLByEntity](../../StoredProcedures/IntegrationStaging/ERP.spOutputShipmentInvoice_TransferXMLByEntity.md)
- [IntegrationStaging: ERP.spShipmentInvoice_TransferXML](../../StoredProcedures/IntegrationStaging/ERP.spShipmentInvoice_TransferXML.md)
- [IntegrationStaging: WMS.spMergeShipmentInvoiceFromPOReceipt](../../StoredProcedures/IntegrationStaging/WMS.spMergeShipmentInvoiceFromPOReceipt.md)

