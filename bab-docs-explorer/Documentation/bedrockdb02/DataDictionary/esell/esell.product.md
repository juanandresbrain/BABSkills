# esell.product

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| product_id | nvarchar | 40 | 0 | YES |  |  |
| product_desc | nvarchar | 2048 | 1 |  |  |  |
| product_name | nvarchar | 80 | 1 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |

