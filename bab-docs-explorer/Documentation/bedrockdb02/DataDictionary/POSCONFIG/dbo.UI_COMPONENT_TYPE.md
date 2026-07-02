# dbo.UI_COMPONENT_TYPE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| COMPONENT_TYPE_CODE | varchar | 10 | 0 |  |  |  |
| DESIGN_CLASS | varchar | 255 | 1 |  |  |  |
| TOOL_BOX_ICON_PATH | nvarchar | 100 | 1 |  |  |  |
| TOOL_TIP_TEXT | nvarchar | 100 | 1 |  |  |  |
| UI_FLG | smallint | 2 | 1 |  |  |  |
| CONTAINER_TYPE_CODE | char | 4 | 1 |  |  |  |
| COMPONENT_TYPE_ID | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.ADD_CONTROLS](../../StoredProcedures/POSCONFIG/dbo.ADD_CONTROLS.md)

