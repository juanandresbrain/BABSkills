# dbo.deleted_style_color

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_color_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| long_desc | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 16 | 0 |  |  |  |
| fashion_flag | bit | 1 | 0 |  |  |  |
| reorder_flag | bit | 1 | 0 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.plu_deleted_style_queue_$sp](../../StoredProcedures/me_01/dbo.plu_deleted_style_queue_$sp.md)
- [me_01: dbo.plu_key_$sp](../../StoredProcedures/me_01/dbo.plu_key_$sp.md)

