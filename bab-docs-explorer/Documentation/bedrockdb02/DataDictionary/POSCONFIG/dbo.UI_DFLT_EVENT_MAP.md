# dbo.UI_DFLT_EVENT_MAP

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| COMPONENT_ID | int | 4 | 0 | YES |  |  |
| EVENT_NAME | varchar | 50 | 0 | YES |  |  |
| PROMPT_DATA | varchar | 50 | 1 |  |  |  |
| FUNCTION_PATH_ID | int | 4 | 1 |  |  |  |
| UI_RESULT_CODE | nvarchar | 150 | 1 |  |  |  |
| CLEAR_PROMPT_FLAG | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)
- [POSCONFIG: dbo.FIND_FUNC_PATH_FLOW](../../StoredProcedures/POSCONFIG/dbo.FIND_FUNC_PATH_FLOW.md)

