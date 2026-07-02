# dbo.DynamicsDiscountSumStage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RetailTransactionId | varchar | 147 | 1 |  |  |  |
| DiscAmount | numeric | 17 | 1 |  |  |  |
| TotalDiscAmount | numeric | 17 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617.md)
- [WebOrderProcessing: dbo.spBabDynamics2_BuildHeaderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics2_BuildHeaderStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics3_BuildSalesLineStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics3_BuildSalesLineStagingTable.md)

