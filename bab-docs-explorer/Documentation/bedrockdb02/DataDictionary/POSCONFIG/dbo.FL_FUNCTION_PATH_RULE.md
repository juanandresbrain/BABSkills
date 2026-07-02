# dbo.FL_FUNCTION_PATH_RULE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| FUNCTION_PATH_ID | int | 4 | 0 | YES |  |  |
| RULE_NAME | varchar | 50 | 0 | YES |  |  |
| RULE_VALUE | nvarchar | 4096 | 1 |  |  |  |
| RULE_EXT_VALUE | ntext | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

