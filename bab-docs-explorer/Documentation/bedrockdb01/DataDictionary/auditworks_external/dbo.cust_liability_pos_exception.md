# dbo.cust_liability_pos_exception

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| issuing_store_no | int | 4 | 0 |  |  |  |
| insert_date | smalldatetime | 4 | 0 |  |  |  |
| pos_amount_1 | money | 8 | 1 |  |  |  |
| pos_amount_2 | money | 8 | 1 |  |  |  |
| pos_amount_3 | money | 8 | 1 |  |  |  |
| pos_status | tinyint | 1 | 1 |  |  |  |
| aw_amount_1 | money | 8 | 1 |  |  |  |
| aw_amount_2 | money | 8 | 1 |  |  |  |
| aw_amount_3 | money | 8 | 1 |  |  |  |
| aw_status | tinyint | 1 | 1 |  |  |  |
| last_synched_date | smalldatetime | 4 | 1 |  |  |  |
| synch_flag | tinyint | 1 | 0 |  |  |  |
| user_name | nvarchar | 100 | 1 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| last_modified | datetime | 8 | 1 |  |  |  |
