# dbo.zzz_ib_allocation_temp3_INC01844615

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_allocation_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| allocated_units | int | 4 | 0 |  |  |  |
| purchase_order_number | nvarchar | 40 | 1 |  |  |  |
| allocation_number | nvarchar | 40 | 1 |  |  |  |

