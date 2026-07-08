# dbo.bk_register_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| register_type | tinyint | 1 | 0 |  |  |  |
| register_type_description | varchar | 50 | 1 |  |  |  |
| proration_method | tinyint | 1 | 0 |  |  |  |
| voiding_disc_multiplier | smallint | 2 | 0 |  |  |  |
| customer_subcode_range_flag | tinyint | 1 | 0 |  |  |  |
| max_transaction_no | int | 4 | 0 |  |  |  |
| display_flag | tinyint | 1 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| transaction_zero_flag | tinyint | 1 | 0 |  |  |  |
