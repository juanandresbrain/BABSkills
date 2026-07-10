# dbo.tmpAWT_SettledNotExported

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SendToSalesExport | int | 4 | 1 |  |  |  |
| order_number | varchar | 32 | 1 |  |  |  |
| SiteCode | nvarchar | 100 | 1 |  |  |  |
| SendToSettlement | int | 4 | 1 |  |  |  |
| DateSentToSettlement | datetime2 | 8 | 1 |  |  |  |
| order_status_code | int | 4 | 0 |  |  |  |
| SettleDate | varchar | 14 | 1 |  |  |  |
