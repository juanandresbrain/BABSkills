# WM.OrderStatus_Archive

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderStatusId | int | 4 | 0 |  |  |  |
| OrderId | int | 4 | 0 |  |  |  |
| Status | varchar | 20 | 1 |  |  |  |
| StatusDate | datetime | 8 | 0 |  |  |  |
| CurrentStatus | bit | 1 | 1 |  |  |  |

