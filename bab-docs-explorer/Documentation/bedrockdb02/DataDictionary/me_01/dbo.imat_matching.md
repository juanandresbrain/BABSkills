# dbo.imat_matching

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_matching_id | decimal | 9 | 0 | YES |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| receipt_number | nvarchar | 40 | 0 |  |  |  |
| gross_matched_amount | decimal | 9 | 0 |  |  |  |
| net_matched_amount | decimal | 9 | 0 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| units_matched | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |

