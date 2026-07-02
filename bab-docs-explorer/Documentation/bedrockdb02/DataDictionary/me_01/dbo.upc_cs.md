# dbo.upc_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| upc_type | tinyint | 1 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| activation_date | smalldatetime | 4 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |

