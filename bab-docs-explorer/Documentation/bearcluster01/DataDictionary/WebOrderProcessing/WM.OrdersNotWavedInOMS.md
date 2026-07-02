# WM.OrdersNotWavedInOMS

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNum | varchar | 10 | 1 |  |  |  |
| WaveDate | datetime | 8 | 1 |  |  |  |
| CheckDateTime | datetime | 8 | 1 |  |  |  |
| ErrorMessage | nvarchar | -1 | 1 |  |  |  |
| LogDateTime | datetime | 8 | 1 |  |  |  |
| Attempts | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spEmailWebOrdersNotWavedInOMS](../../StoredProcedures/WebOrderProcessing/WM.spEmailWebOrdersNotWavedInOMS.md)

