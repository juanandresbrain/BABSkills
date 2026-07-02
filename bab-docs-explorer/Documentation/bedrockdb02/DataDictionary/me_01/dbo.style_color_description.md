# dbo.style_color_description

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_color_description_id | decimal | 9 | 0 | YES |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |
| language_id | int | 4 | 0 |  |  |  |
| long_desc | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 16 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)

