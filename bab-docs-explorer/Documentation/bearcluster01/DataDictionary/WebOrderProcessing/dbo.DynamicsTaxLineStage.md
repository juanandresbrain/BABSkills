# dbo.DynamicsTaxLineStage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 136 | 1 |  |  |  |
| Amount | numeric | 9 | 1 |  |  |  |
| LineNum | varchar | 50 | 1 |  |  |  |
| TaxCode | varchar | 3 | 0 |  |  |  |
| RetailTerminalId | varchar | 53 | 1 |  |  |  |
| RetailTransactionId | varchar | 138 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 14 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| CreateTime | datetime | 8 | 1 |  |  |  |
| Barcode | varchar | 50 | 1 |  |  |  |
| InventLocationId | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics4_BuildTaxStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics4_BuildTaxStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics6_BlankSoundChipInsert](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics6_BlankSoundChipInsert.md)
- [WebOrderProcessing: dbo.spBabDynamics7_ShippingLineInserts](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics7_ShippingLineInserts.md)

