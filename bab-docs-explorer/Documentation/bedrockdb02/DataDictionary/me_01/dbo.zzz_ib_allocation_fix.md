# dbo.zzz_ib_allocation_fix

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| allocation_number | nvarchar | 40 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| allocated_units | int | 4 | 1 |  |  |  |

