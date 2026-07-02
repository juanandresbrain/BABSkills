# dbo.imat_process_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_process_detail_id | decimal | 9 | 0 | YES |  |  |
| imat_process_header_id | decimal | 9 | 0 |  |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| imat_flow_id | decimal | 9 | 0 |  |  |  |
| imat_match_process_id | tinyint | 1 | 0 |  |  |  |
| imat_match_option_id | tinyint | 1 | 1 |  |  |  |
| imat_match_result_id | tinyint | 1 | 0 |  |  |  |
| match_discount_amount | decimal | 9 | 1 |  |  |  |
| error | bit | 1 | 0 |  |  |  |

