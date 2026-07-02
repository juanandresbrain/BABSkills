# esell.inventory_status

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| sku_inv_col_name | nvarchar | 36 | 0 | YES |  |  |
| inv_short_name | nvarchar | 10 | 1 |  |  |  |
| inv_long_name | nvarchar | 40 | 1 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |

