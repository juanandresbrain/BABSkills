# dbo.shap_if_rejection_reason

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| deferred | tinyint | 1 | 0 |  |  |  |
| memo1 | varchar | 255 | 1 |  |  |  |
| memo2 | varchar | 255 | 1 |  |  |  |
| memo3 | varchar | 255 | 1 |  |  |  |
| replace_upc_no | numeric | 9 | 1 |  |  |  |
| replace_line_object | smallint | 2 | 1 |  |  |  |
| replace_line_action | smallint | 2 | 1 |  |  |  |
| process_id | int | 4 | 1 |  |  |  |
| lookup_key1 | int | 4 | 1 |  |  |  |
| other_information | varchar | 255 | 1 |  |  |  |
| tab_delimited_token_list | varchar | 255 | 1 |  |  |  |
