# dbo.UI_SCREEN

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| SCREEN_ID | int | 4 | 0 | YES |  |  |
| SCREEN_TYPE | char | 4 | 1 |  |  |  |
| SCREEN_NAME | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)
- [POSCONFIG: dbo.FIND_FUNC_PATH_FLOW](../../StoredProcedures/POSCONFIG/dbo.FIND_FUNC_PATH_FLOW.md)

