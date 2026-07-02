# dbo.po_special_order

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_special_order_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| so_number | nvarchar | 40 | 1 |  |  |  |
| customer_name | nvarchar | 60 | 0 |  |  |  |
| address1 | nvarchar | 100 | 1 |  |  |  |
| address2 | nvarchar | 100 | 1 |  |  |  |
| city | nvarchar | 40 | 1 |  |  |  |
| state | nvarchar | 40 | 1 |  |  |  |
| country_id | decimal | 9 | 1 |  | YES |  |
| zip_code | nvarchar | 30 | 1 |  |  |  |
| member_number | nvarchar | 40 | 1 |  |  |  |
| sa_number | nvarchar | 40 | 1 |  |  |  |
| sa_name | nvarchar | 60 | 1 |  |  |  |

