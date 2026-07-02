# dbo.parameter_plu

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_plu_id | tinyint | 1 | 0 | YES |  |  |
| parameter_name | nvarchar | 80 | 0 |  |  |  |
| parameter_group_plu_id | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.plu_dept_params_$sp](../../StoredProcedures/me_01/dbo.plu_dept_params_$sp.md)

