# dbo.style_assignment_plu

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_assignment_plu_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| parameter_group_plu_id | decimal | 9 | 0 |  |  |  |
| attribute_set_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| style_size_id | decimal | 9 | 1 |  |  |  |
| group_permutation_plu_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.plu_style_queue_$sp](../../StoredProcedures/me_01/dbo.plu_style_queue_$sp.md)

