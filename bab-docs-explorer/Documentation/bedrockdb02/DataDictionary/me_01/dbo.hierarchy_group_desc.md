# dbo.hierarchy_group_desc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_desc_id | decimal | 9 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| language_id | int | 4 | 0 |  |  |  |
| hierarchy_group_label | nvarchar | 80 | 0 |  |  |  |
| hierarchy_group_short_label | nvarchar | 40 | 0 |  |  |  |
| plu_description | nvarchar | 80 | 1 |  |  |  |
| plu_dept_group_description | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.plu_crs_temp_output_$sp](../../StoredProcedures/me_01/dbo.plu_crs_temp_output_$sp.md)
- [me_01: dbo.plu_dept_queue_$sp](../../StoredProcedures/me_01/dbo.plu_dept_queue_$sp.md)

