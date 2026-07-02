# dbo.eom_reserve_transaction

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| batch_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| outlet_id | smallint | 2 | 0 |  |  |  |
| cust_order_no | nvarchar | 40 | 0 |  |  |  |
| requested_reserve_quantity | int | 4 | 0 |  |  |  |
| transaction_type | smallint | 2 | 0 |  |  |  |
| transaction_cancelled | bit | 1 | 0 |  |  |  |
| processed_date | datetime | 8 | 0 |  |  |  |
| outlet_code | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)

