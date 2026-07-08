# dbo.input_line_note

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| note_type | smallint | 2 | 0 |  |  |  |
| line_note | nvarchar | 6000 | 0 |  |  |  |
| lookup_pos_code | nvarchar | 40 | 1 |  |  |  |
| pos_description | nvarchar | 510 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
