# dbo.employee_comms_auto_adj_calc

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| auto_commission_adj_id | numeric | 5 | 0 |  |  |  |
| auto_commission_adj_line_id | numeric | 9 | 0 | YES |  |  |
| adjustment_line_type | nvarchar | 20 | 0 |  |  |  |
| adjustment_line_sequence | smallint | 2 | 1 |  |  |  |
| parenthesis_prefix | nvarchar | 40 | 0 |  |  |  |
| comparison_type | smallint | 2 | 1 |  |  |  |
| accumulation_basis | smallint | 2 | 1 |  |  |  |
| constant_value | money | 8 | 1 |  |  |  |
| parenthesis_suffix | nvarchar | 40 | 0 |  |  |  |
| operator | nvarchar | 6 | 0 |  |  |  |
