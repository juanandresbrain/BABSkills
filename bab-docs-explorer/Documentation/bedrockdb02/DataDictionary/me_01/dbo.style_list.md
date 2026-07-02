# dbo.style_list

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_list_id | decimal | 9 | 0 | YES |  |  |
| style_list_name | nvarchar | 40 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| send_to_eom | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)

