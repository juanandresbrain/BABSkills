# WM.OrdersNotOnColumbusDB

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 10 | 1 |  |  |  |
| WaveDateTime | datetime | 8 | 1 |  |  |  |
| CheckDateTime | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spEmailOrdersNotOnColumbusDB](../../StoredProcedures/WebOrderProcessing/WM.spEmailOrdersNotOnColumbusDB.md)

