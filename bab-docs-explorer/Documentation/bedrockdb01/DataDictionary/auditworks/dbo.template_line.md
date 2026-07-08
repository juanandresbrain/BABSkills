# dbo.template_line

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| template_id | tran_id_datatype | 9 | 0 |  |  |  |
| template_sequence | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| gross_line_amount | line_amount_18_4 | 9 | 0 |  |  |  |
