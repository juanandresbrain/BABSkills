# dbo.employee_preference

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| context_id | int | 4 | 0 |  |  |  |
| employee_id | decimal | 9 | 1 |  |  |  |
| preference_label | nvarchar | 510 | 1 |  |  |  |
| preference_definition_xml | nvarchar | -1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

