# WMS.PartyToDynamics

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyId | nvarchar | 20 | 1 |  |  |  |
| FromWarehouse | varchar | 4 | 0 |  |  |  |
| ToWarehouse | varchar | 5 | 1 |  |  |  |
| LineNumber | int | 4 | 1 |  |  |  |
| ItemNumber | nvarchar | 20 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| UnitOfMeasure | varchar | 2 | 0 |  |  |  |
| Company | varchar | 4 | 0 |  |  |  |
| CountryCode | int | 4 | 1 |  |  |  |
| DeliveryTerms | varchar | 10 | 0 |  |  |  |
| ModeOfDelivery | varchar | 100 | 1 |  |  |  |
| OrderType | varchar | 13 | 0 |  |  |  |
| ShipDate | varchar | 10 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| PartyDate | varchar | 30 | 1 |  |  |  |
| InventoryStatus | varchar | 5 | 0 |  |  |  |
| AptosDistroNumber | int | 4 | 1 |  |  |  |
| SourceCountry | varchar | 2 | 0 |  |  |  |
| DestinationCountry | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreShipmentExportParty](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreShipmentExportParty.md)
- [IntegrationStaging: WMS.spPartyStageForDynamics](../../StoredProcedures/IntegrationStaging/WMS.spPartyStageForDynamics.md)

