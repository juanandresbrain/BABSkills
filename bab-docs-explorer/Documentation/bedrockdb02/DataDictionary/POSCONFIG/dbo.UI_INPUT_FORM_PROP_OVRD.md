# dbo.UI_INPUT_FORM_PROP_OVRD

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| INPUT_FORM_ID | int | 4 | 0 | YES |  |  |
| CONTROL_ID | int | 4 | 0 | YES |  |  |
| OVRD_SEQ_NO | smallint | 2 | 0 | YES |  |  |
| PROP_NAME | varchar | 50 | 0 |  |  |  |
| CONDITION | nvarchar | -1 | 1 |  |  |  |
| PROP_OVERRIDE_VALUE | nvarchar | 510 | 1 |  |  |  |
| OVRD_NAME | nvarchar | 100 | 1 |  |  |  |

