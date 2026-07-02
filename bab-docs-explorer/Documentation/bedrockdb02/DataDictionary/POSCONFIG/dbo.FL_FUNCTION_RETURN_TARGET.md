# dbo.FL_FUNCTION_RETURN_TARGET

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| FUNCTION_PATH_ID | int | 4 | 0 | YES |  |  |
| RETURN_CODE | int | 4 | 0 | YES |  |  |
| TARGET_TYPE | char | 4 | 1 |  |  |  |
| TARGET_STATE_ID | int | 4 | 1 |  |  |  |
| TARGET_FN_PATH_ID | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)
- [POSCONFIG: dbo.FIND_FUNC_PATH_FLOW](../../StoredProcedures/POSCONFIG/dbo.FIND_FUNC_PATH_FLOW.md)

