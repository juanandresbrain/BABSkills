# dbo.transaction_reason_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_reason_id | smallint | 2 | 0 | YES |  |  |
| transaction_reason_code | nvarchar | 10 | 0 |  |  |  |
| transaction_reason_desc | nvarchar | 80 | 0 |  |  |  |
| user_defined_flag | bit | 1 | 0 |  |  |  |
| reason_type_id | smallint | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.post_25Nov25_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_25Nov25_cust_order_sale_$sp.md)
- [me_01: dbo.post_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_sale_$sp.md)

