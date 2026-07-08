# dbo.template_attachment

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| template_id | tran_id_datatype | 9 | 0 |  |  |  |
| template_sequence | numeric | 5 | 0 |  |  |  |
| attachment_type | smallint | 2 | 0 |  |  |  |
| attachment_type_note_type | int | 4 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| salesperson1 | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
