# ComHub.xmlFile

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| xmlFileId | int | 4 | 0 | YES |  |  |
| xmlFileName | varchar | 255 | 0 |  |  |  |
| xmlTypeId | int | 4 | 0 |  | YES |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoConfirmations](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoConfirmations.md)
- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoFAs](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoFAs.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersAcknowledged](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersAcknowledged.md)
- [WebOrderProcessing: ComHub.spUpdatePOWebOrdersFulFilled](../../StoredProcedures/WebOrderProcessing/ComHub.spUpdatePOWebOrdersFulFilled.md)

