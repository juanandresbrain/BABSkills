# dbo.POSProducts

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductSellingGeography | varchar | 2 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| ItemName | varchar | 120 | 1 |  |  |  |
| Sound | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics6_BlankSoundChipInsert](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics6_BlankSoundChipInsert.md)
- [WebOrderProcessing: dbo.spMergePOSProducts](../../StoredProcedures/WebOrderProcessing/dbo.spMergePOSProducts.md)

