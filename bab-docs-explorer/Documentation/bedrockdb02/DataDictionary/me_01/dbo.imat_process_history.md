# dbo.imat_process_history

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_process_history_id | decimal | 9 | 0 | YES |  |  |
| imat_process_header_id | decimal | 9 | 0 |  |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| imat_match_process_id | tinyint | 1 | 0 |  |  |  |
| imat_match_result_id | tinyint | 1 | 0 |  |  |  |
| imat_match_option_id | tinyint | 1 | 0 |  |  |  |
| datetimestamp | smalldatetime | 4 | 0 |  |  |  |

