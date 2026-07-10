# dbo.tmpAWT_ShippedNotSettled

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_status_code | int | 4 | 0 |  |  |  |
| SendToSettlement | int | 4 | 1 |  |  |  |
| productionorderdatetimeShipped | datetime | 8 | 1 |  |  |  |
| DateTimeShipped | varchar | 14 | 1 |  |  |  |
| productionOrderNumber | varchar | 32 | 0 |  |  |  |
| order_number | varchar | 32 | 1 |  |  |  |
| SiteCode | nvarchar | 100 | 1 |  |  |  |
