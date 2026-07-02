# dbo.es_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)

