# dbo.UI_LOCALIZATION_SCOPE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SCOPE_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| FLOW_ID | int | 4 | 1 |  |  |  |
| PARENT_TYPE | nvarchar | 100 | 1 |  |  |  |
| PARENT_ID | nvarchar | 200 | 1 |  |  |  |
| PROPERTY_TYPE | nvarchar | 100 | 1 |  |  |  |
| PROPERTY_ID | nvarchar | 200 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

