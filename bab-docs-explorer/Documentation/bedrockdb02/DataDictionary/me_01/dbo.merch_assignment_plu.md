# dbo.merch_assignment_plu

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_assignment_plu_id | decimal | 9 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| parameter_group_plu_id | decimal | 9 | 0 |  |  |  |
| attribute_set_id | decimal | 9 | 0 |  |  |  |
| group_permutation_plu_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.plu_dept_params_$sp](../../StoredProcedures/me_01/dbo.plu_dept_params_$sp.md)
- [me_01: dbo.plu_hg_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_queue_$sp.md)

