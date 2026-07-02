# dbo.UI_LOCALIZED_RESOURCE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LOCALIZED_RESOURCE_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| DEFAULT_VALUE | nvarchar | 3000 | 0 |  |  |  |
| RESOURCE_TYPE | varchar | 10 | 0 |  |  |  |
| LANGUAGE_CODE | varchar | 10 | 0 |  |  |  |
| SCOPE_ID | uniqueidentifier | 16 | 0 |  |  |  |
| LOCALIZED_VALUE | nvarchar | 3000 | 0 |  |  |  |
| DEFAULT_VALUE_HASH | varbinary | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

