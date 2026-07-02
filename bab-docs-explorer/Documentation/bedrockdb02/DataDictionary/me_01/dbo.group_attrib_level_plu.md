# dbo.group_attrib_level_plu

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| group_attrib_level_plu_id | decimal | 9 | 0 | YES |  |  |
| parameter_group_plu_id | decimal | 9 | 0 |  |  |  |
| attribute_id | decimal | 9 | 0 |  |  |  |
| hierarchy_level_id | int | 4 | 0 |  |  |  |
| department_data | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.plu_dept_params_$sp](../../StoredProcedures/me_01/dbo.plu_dept_params_$sp.md)
- [me_01: dbo.plu_hg_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_queue_$sp.md)

