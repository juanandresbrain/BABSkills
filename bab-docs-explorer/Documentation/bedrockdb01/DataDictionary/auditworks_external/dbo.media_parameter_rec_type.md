# dbo.media_parameter_rec_type

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 0 |  |  |  |
| dflt_short_tolerance_amount | money | 8 | 0 |  |  |  |
| dflt_short_tolerance_qty | int | 4 | 0 |  |  |  |
| dflt_short_tolerance_percent | numeric | 5 | 0 |  |  |  |
| dflt_unrec_tolerance_days | smallint | 2 | 0 |  |  |  |
| dflt_unrec_tolerance_amount | money | 8 | 0 |  |  |  |
| auto_populate_object | tinyint | 1 | 0 |  |  |  |
