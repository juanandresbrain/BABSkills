# dbo.DynamicsTargetTransactions

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 10 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics0_BuildTargetTransactionsTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics0_BuildTargetTransactionsTable.md)
- [WebOrderProcessing: dbo.spBabDynamics1_BuildDiscountStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics1_BuildDiscountStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics2_BuildHeaderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics2_BuildHeaderStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics3_BuildSalesLineStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics3_BuildSalesLineStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics4_BuildTaxStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics4_BuildTaxStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics5_BuildTenderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics5_BuildTenderStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics7_ShippingLineInserts](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics7_ShippingLineInserts.md)

