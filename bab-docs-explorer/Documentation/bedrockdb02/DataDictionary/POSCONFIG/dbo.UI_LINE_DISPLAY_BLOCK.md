# dbo.UI_LINE_DISPLAY_BLOCK

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| LINE_BLOCK_TYPE_CODE | varchar | 20 | 0 | YES |  |  |
| CONFIG_ID | int | 4 | 0 | YES |  |  |
| SCRIPT | ntext | 16 | 1 |  |  |  |
| INTER_CHARACTER_WAIT | int | 4 | 1 |  |  |  |
| MARQUEE_REPEAT_WAIT | int | 4 | 1 |  |  |  |
| MARQUEE_UNIT_WAIT | int | 4 | 1 |  |  |  |
| MODE | smallint | 2 | 1 |  |  |  |
| MARQUEE_FORMAT | smallint | 2 | 1 |  |  |  |
| MARQUEE_TYPE | smallint | 2 | 1 |  |  |  |
| WINDOW_NO | smallint | 2 | 1 |  |  |  |
| COMPONENT_ID | int | 4 | 1 |  |  |  |
| LINE_WIDTH | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

