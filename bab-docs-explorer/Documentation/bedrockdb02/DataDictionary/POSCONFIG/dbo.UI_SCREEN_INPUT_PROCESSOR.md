# dbo.UI_SCREEN_INPUT_PROCESSOR

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| SCREEN_ID | int | 4 | 0 | YES |  |  |
| SEQUENCE_NO | smallint | 2 | 0 | YES |  |  |
| PROCESSOR_CLASS | varchar | 255 | 1 |  |  |  |
| PROCESSOR_RULES | varchar | 6500 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

