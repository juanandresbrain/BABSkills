# dbo.UI_LINE_DISPLAY_RECEIPT

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CONFIG_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| FLOW_ID | int | 4 | 0 | YES |  |  |
| COMPONENT_ID | int | 4 | 0 |  |  |  |
| WINDOW_NO | smallint | 2 | 1 |  |  |  |
| LINE_WIDTH | smallint | 2 | 1 |  |  |  |
| NUM_LINES | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

