# WM.OrdersSentToWM

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WMFileName | varchar | 50 | 1 |  |  |  |
| OrderNum | varchar | 10 | 1 |  |  |  |
| SendTime | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spInsertOrderSentToWM](../../StoredProcedures/WebOrderProcessing/WM.spInsertOrderSentToWM.md)

