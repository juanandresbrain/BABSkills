# dbo.FL_STATE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| STATE_ID | int | 4 | 0 | YES |  |  |
| NAME | varchar | 50 | 1 |  |  |  |
| DESCRIPTION | varchar | 50 | 1 |  |  |  |
| INIT_FUNC_PATH_ID | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

