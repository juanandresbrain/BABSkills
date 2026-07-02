# dbo.sku_customer_back_order

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 0 | YES |  |  |
| allow_customer_back_order | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.cascade_allow_customer_back_order_to_skus_$sp](../../StoredProcedures/me_01/dbo.cascade_allow_customer_back_order_to_skus_$sp.md)

