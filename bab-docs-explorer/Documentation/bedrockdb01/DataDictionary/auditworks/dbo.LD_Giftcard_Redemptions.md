# dbo.LD_Giftcard_Redemptions

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
