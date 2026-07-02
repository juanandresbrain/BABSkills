# dbo.imp_ib_user_def_adj_dtl

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_ib_user_def_adj_dtl_id | decimal | 9 | 0 | YES |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| submit_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_reason_code | nvarchar | 10 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| inventory_status_code | nvarchar | 6 | 0 |  |  |  |
| imp_ib_user_def_adj_id | decimal | 9 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |

