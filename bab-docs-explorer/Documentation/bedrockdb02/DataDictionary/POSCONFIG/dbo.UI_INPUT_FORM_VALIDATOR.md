# dbo.UI_INPUT_FORM_VALIDATOR

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| INPUT_FORM_ID | int | 4 | 0 | YES |  |  |
| CONTROL_ID | int | 4 | 0 | YES |  |  |
| SEQUENCE_NO | smallint | 2 | 0 | YES |  |  |
| VALIDATOR_NAME | varchar | 50 | 1 |  |  |  |
| VALIDATOR_CLASS | varchar | 255 | 1 |  |  |  |
| VALIDATOR_RULES | varchar | 6500 | 1 |  |  |  |

