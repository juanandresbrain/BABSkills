# dbo.Sv_Mail

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mail_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| send_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| send_date | smalldatetime | 4 | 0 |  |  |  |
| read_date | smalldatetime | 4 | 1 |  |  |  |
| message | text | 16 | 1 |  |  |  |
| attached_type | smallint | 2 | 0 |  |  |  |
| attached_id | int | 4 | 0 |  |  |  |
| output_data | varchar | 100 | 1 |  |  |  |
| crosstab_data | varchar | 100 | 1 |  |  |  |
| graph_data | varchar | 100 | 1 |  |  |  |
| default_data_view | char | 1 | 0 |  |  |  |
