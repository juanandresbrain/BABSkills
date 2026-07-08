# dbo.awl_customer_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| customer_role | smallint | 2 | 0 |  |  |  |
| customer_info_type | smallint | 2 | 0 |  |  |  |
| customer_info | nvarchar | 8000 | 0 |  |  |  |
| lookup_pos_code | nvarchar | 40 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| auto_config_verified | tinyint | 1 | 1 |  |  |  |
