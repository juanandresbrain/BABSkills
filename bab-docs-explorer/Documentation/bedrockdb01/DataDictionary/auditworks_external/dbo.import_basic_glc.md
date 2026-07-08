# dbo.import_basic_glc

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| glc_type | tinyint | 1 | 0 |  |  |  |
| tracking_id | smallint | 2 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| customer_liability_action_no | numeric | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| object | smallint | 2 | 0 |  |  |  |
| action | smallint | 2 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
