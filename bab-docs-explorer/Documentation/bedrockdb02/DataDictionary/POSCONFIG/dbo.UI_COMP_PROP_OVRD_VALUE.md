# dbo.UI_COMP_PROP_OVRD_VALUE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| SCREEN_ID | int | 4 | 0 | YES |  |  |
| COMPONENT_ID | int | 4 | 0 | YES |  |  |
| OVRD_SEQ_NO | smallint | 2 | 0 | YES |  |  |
| PROP_NAME | varchar | 50 | 0 |  |  |  |
| CONDITION | nvarchar | -1 | 1 |  |  |  |
| PROP_OVERRIDE_VALUE | nvarchar | 7000 | 1 |  |  |  |
| OVRD_NAME | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

