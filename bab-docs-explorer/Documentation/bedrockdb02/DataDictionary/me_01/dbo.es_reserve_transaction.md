# dbo.es_reserve_transaction

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| es_reserve_transaction_id | bigint | 8 | 0 | YES |  |  |
| transaction_id | bigint | 8 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| cust_order_no | nvarchar | 40 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| selling_retail | float | 8 | 1 |  |  |  |
| valuation_retail | float | 8 | 1 |  |  |  |
| average_cost | float | 8 | 1 |  |  |  |
| average_cost_local | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.es_reserve_$sp](../../StoredProcedures/me_01/dbo.es_reserve_$sp.md)

