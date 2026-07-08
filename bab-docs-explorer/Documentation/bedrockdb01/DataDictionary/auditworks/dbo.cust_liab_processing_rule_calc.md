# dbo.cust_liab_processing_rule_calc

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rule_id | nvarchar | 6 | 0 |  |  |  |
| processing_rule_calc_line_id | numeric | 9 | 0 | YES |  |  |
| adjustment_line_type | nvarchar | 20 | 0 |  |  |  |
| adjustment_line_sequence | smallint | 2 | 1 |  |  |  |
| parenthesis_prefix | nvarchar | 40 | 0 |  |  |  |
| unit_amount_flag | tinyint | 1 | 1 |  |  |  |
| column_no | tinyint | 1 | 1 |  |  |  |
| constant_value | money | 8 | 1 |  |  |  |
| constant_date | datetime | 8 | 1 |  |  |  |
| parenthesis_suffix | nvarchar | 40 | 0 |  |  |  |
| operator | nvarchar | 6 | 0 |  |  |  |
