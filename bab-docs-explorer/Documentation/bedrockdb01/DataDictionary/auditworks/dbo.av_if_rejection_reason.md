# dbo.av_if_rejection_reason

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| deferred | tinyint | 1 | 0 |  |  |  |
| memo1 | nvarchar | 510 | 1 |  |  |  |
| memo2 | nvarchar | 510 | 1 |  |  |  |
| memo3 | nvarchar | 510 | 1 |  |  |  |
| replace_upc_no | numeric | 9 | 1 |  |  |  |
| replace_line_object | smallint | 2 | 1 |  |  |  |
| replace_line_action | smallint | 2 | 1 |  |  |  |
| process_id | binary | 16 | 1 |  |  |  |
| lookup_key1 | int | 4 | 1 |  |  |  |
| other_information | nvarchar | 510 | 1 |  |  |  |
| tab_delimited_token_list | nvarchar | 510 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
