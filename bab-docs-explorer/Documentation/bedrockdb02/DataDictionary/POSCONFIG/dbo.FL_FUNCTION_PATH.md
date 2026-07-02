# dbo.FL_FUNCTION_PATH

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| FUNCTION_PATH_ID | int | 4 | 0 | YES |  |  |
| NAME | varchar | 50 | 1 |  |  |  |
| DESCRIPTION | varchar | 50 | 1 |  |  |  |
| FUNCTION_ID | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)
- [POSCONFIG: dbo.FIND_FUNC_PATH_FLOW](../../StoredProcedures/POSCONFIG/dbo.FIND_FUNC_PATH_FLOW.md)

