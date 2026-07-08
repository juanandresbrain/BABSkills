# dbo.work_media_para_rec_group

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | int | 4 | 0 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| short_tolerance_amount | money | 8 | 0 |  |  |  |
| short_tolerance_qty | int | 4 | 0 |  |  |  |
| short_tolerance_percent | numeric | 5 | 0 |  |  |  |
| unrec_tolerance_days | smallint | 2 | 0 |  |  |  |
| unrec_tolerance_amount | money | 8 | 0 |  |  |  |
| rec_option | smallint | 2 | 0 |  |  |  |
| track_qty | tinyint | 1 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
