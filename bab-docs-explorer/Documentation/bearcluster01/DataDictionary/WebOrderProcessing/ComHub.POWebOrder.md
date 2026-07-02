# ComHub.POWebOrder

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| POWebOrderId | int | 4 | 0 | YES |  |  |
| OrderMessageBatch | bigint | 8 | 1 |  |  |  |
| TransactionId | bigint | 8 | 0 |  |  |  |
| PONumber | varchar | 20 | 0 |  |  |  |
| OrderId | int | 4 | 1 |  |  |  |
| POjson | varchar | -1 | 1 |  |  |  |
| CreatedBy | varchar | 255 | 0 |  |  |  |
| CreatedOn | datetime | 8 | 0 |  |  |  |
| FAxmlId | int | 4 | 1 |  | YES |  |
| ConfirmationXmlId | int | 4 | 1 |  | YES |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoConfirmations](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoConfirmations.md)
- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoFAs](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoFAs.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersAcknowledged](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersAcknowledged.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersFulFilled](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersFulFilled.md)

