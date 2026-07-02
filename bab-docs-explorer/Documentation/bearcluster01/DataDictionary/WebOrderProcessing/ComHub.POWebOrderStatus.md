# ComHub.POWebOrderStatus

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| POWebOrderStatusId | int | 4 | 0 | YES |  |  |
| POWebOrderId | int | 4 | 0 |  | YES |  |
| StatusId | int | 4 | 0 |  | YES |  |
| CreatedBy | varchar | 255 | 0 |  |  |  |
| CreatedOn | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoConfirmations](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoConfirmations.md)
- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoFAs](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoFAs.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersAcknowledged](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersAcknowledged.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersFulFilled](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersFulFilled.md)

