# dbo.av_line_note

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| note_type | smallint | 2 | 0 |  |  |  |
| line_note | nvarchar | 8000 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
