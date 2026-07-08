# dbo.employee_comms_auto_adj

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| auto_commission_adj_id | numeric | 5 | 0 | YES |  |  |
| auto_adjustment_description | nvarchar | 510 | 0 |  |  |  |
| adjustment_sequence | smallint | 2 | 1 |  |  |  |
| adjustment_calendar_level | smallint | 2 | 0 |  |  |  |
| auto_reversal_flag | tinyint | 1 | 0 |  |  |  |
| auto_rev_except_calendr_level | smallint | 2 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| custom_adjustment_flag | tinyint | 1 | 0 |  |  |  |
| custom_stored_proc_name | nvarchar | 60 | 1 |  |  |  |
| adjustment_comment | nvarchar | 2000 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| post_zero_amt_flag | tinyint | 1 | 0 |  |  |  |
| reference_amount_type | smallint | 2 | 1 |  |  |  |
