# dbo.UI_COMPONENT_PROP

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| COMPONENT_ID | int | 4 | 0 | YES |  |  |
| PROP_NAME | varchar | 50 | 0 | YES |  |  |
| PROP_DFLT_VALUE | nvarchar | 7000 | 1 |  |  |  |
| PREPROCESS_FLAG | smallint | 2 | 1 |  |  |  |
| LOCALIZABLE_FLAG | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

