# esell.order_state

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_state | nvarchar | 40 | 0 | YES |  |  |
| order_state_name | nvarchar | 80 | 0 |  |  |  |
| order_state_desc | nvarchar | 510 | 0 |  |  |  |
| modify_allowed | nchar | 2 | 0 |  |  |  |
| state_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.spES_Aged_Orders_Check](../../StoredProcedures/esell/dbo.spES_Aged_Orders_Check.md)

