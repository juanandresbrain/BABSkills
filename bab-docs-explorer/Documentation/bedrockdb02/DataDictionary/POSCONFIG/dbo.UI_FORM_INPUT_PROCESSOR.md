# dbo.UI_FORM_INPUT_PROCESSOR

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| INPUT_FORM_ID | int | 4 | 0 | YES |  |  |
| SEQUENCE_NO | smallint | 2 | 0 | YES |  |  |
| PARSER_NAME | varchar | 50 | 1 |  |  |  |
| TRIGGER_CONTROLS | varchar | 1000 | 1 |  |  |  |
| PROCESSOR_CLASS | varchar | 255 | 1 |  |  |  |
| PROCESSOR_RULES | varchar | 6500 | 1 |  |  |  |
| UI_RESULT_CODE | nvarchar | 150 | 1 |  |  |  |
| DISMISS_FORM_FLG | smallint | 2 | 1 |  |  |  |
| CAUSES_VALIDATION_FLG | smallint | 2 | 1 |  |  |  |
| CAUSES_SVR_VALIDATION_FLG | smallint | 2 | 1 |  |  |  |
| WAIT_CURSOR_FLG | smallint | 2 | 1 |  |  |  |
| MOVE_TO_CONTROL | varchar | 100 | 1 |  |  |  |

