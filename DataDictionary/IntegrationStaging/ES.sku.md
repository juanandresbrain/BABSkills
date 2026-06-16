# ES.sku

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| sku_id | nvarchar | 48 | 0 | YES |  |  |
| sku_price | int | 4 | 1 |  |  |  |
| product_id | nvarchar | 40 | 1 |  |  |  |
| inv_ver_req_cd | nchar | 2 | 1 |  |  |  |
| barcode | nvarchar | 100 | 1 |  |  |  |
| upc | nvarchar | 100 | 1 |  |  |  |
| pick_desc | nvarchar | 160 | 1 |  |  |  |
| sku_avail_date | datetime | 8 | 1 |  |  |  |
| sku_unavail_date | datetime | 8 | 1 |  |  |  |
| search_allowed_cd | nchar | 2 | 1 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |
| department_id | int | 4 | 0 |  |  |  |

