# dbo.media_category_statistics

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| media_category | tinyint | 1 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| transaction_qty | real | 4 | 0 |  |  |  |
| transaction_qty_adj | real | 4 | 0 |  |  |  |
