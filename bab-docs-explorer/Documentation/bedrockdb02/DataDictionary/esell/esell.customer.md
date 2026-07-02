# esell.customer

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_id | nvarchar | 60 | 0 | YES |  |  |
| customer_id | nvarchar | 40 | 0 | YES |  |  |
| cust_type | nvarchar | 40 | 0 | YES |  |  |
| first_name | nvarchar | 60 | 1 |  |  |  |
| middle_name | nvarchar | 60 | 1 |  |  |  |
| last_name | nvarchar | 60 | 1 |  |  |  |
| day_phone | nvarchar | 40 | 1 |  |  |  |
| evening_phone | nvarchar | 40 | 1 |  |  |  |
| email | nvarchar | 500 | 1 |  |  |  |
| fax | nvarchar | 40 | 1 |  |  |  |
| address1 | nvarchar | 200 | 1 |  |  |  |
| address2 | nvarchar | 200 | 1 |  |  |  |
| city | nvarchar | 120 | 1 |  |  |  |
| state | nvarchar | 40 | 1 |  |  |  |
| postal_code | nvarchar | 30 | 1 |  |  |  |
| country | nchar | 6 | 1 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |
| mobile_phone | nvarchar | 40 | 1 |  |  |  |

