# ComHub.Status

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StatusId | int | 4 | 0 | YES |  |  |
| Keyword | varchar | 50 | 0 |  |  |  |
| Description | varchar | 255 | 0 |  |  |  |
| StatusOrder | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoConfirmations](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoConfirmations.md)
- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoFAs](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoFAs.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersAcknowledged](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersAcknowledged.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersFulFilled](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersFulFilled.md)

