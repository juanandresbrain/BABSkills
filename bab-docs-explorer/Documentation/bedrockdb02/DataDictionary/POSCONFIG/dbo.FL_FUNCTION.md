# dbo.FL_FUNCTION

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FUNCTION_ID | int | 4 | 0 | YES |  |  |
| NAME | varchar | 50 | 1 |  |  |  |
| DESCRIPTION | varchar | 255 | 1 |  |  |  |
| FUNCTION_CLASS | varchar | 255 | 1 |  |  |  |
| RULES_CLASS | varchar | 255 | 1 |  |  |  |
| PARAMETERS_CLASS | varchar | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.FIND_FUNC_PATH_FLOW](../../StoredProcedures/POSCONFIG/dbo.FIND_FUNC_PATH_FLOW.md)

