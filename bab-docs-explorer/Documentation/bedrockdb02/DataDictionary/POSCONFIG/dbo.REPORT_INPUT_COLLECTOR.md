# dbo.REPORT_INPUT_COLLECTOR

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| REPORT_ID | int | 4 | 0 | YES |  |  |
| CLASS_NAME | varchar | 255 | 0 | YES |  |  |
| DESCRIPTION | nvarchar | 510 | 1 |  |  |  |
| APP_ORDER | int | 4 | 1 |  |  |  |
| INPUT_FORM_NAME | nvarchar | 510 | 1 |  |  |  |
| ACTION_MODE | smallint | 2 | 0 |  |  |  |
| VISIBILITY_MODE | smallint | 2 | 0 |  |  |  |
| RULES | ntext | 16 | 1 |  |  |  |
| PARAMETERS | ntext | 16 | 1 |  |  |  |

