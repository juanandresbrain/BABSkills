# dbo.tmpUKpartnerOperatedTransferOrder

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| ModeOfDelivery | varchar | 8000 | 1 |  |  |  |
| ItemID | varchar | 8000 | 1 |  |  |  |
| ItemDescription | varchar | 8000 | 1 |  |  |  |
| ShippedQuantity | numeric | 9 | 1 |  |  |  |
| DateTime | varchar | 30 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailUKpartnerOperatedTransferOrder](../../StoredProcedures/IntegrationStaging/WMS.spEmailUKpartnerOperatedTransferOrder.md)

