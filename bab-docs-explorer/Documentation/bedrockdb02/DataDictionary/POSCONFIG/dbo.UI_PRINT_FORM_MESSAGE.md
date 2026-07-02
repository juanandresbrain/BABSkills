# dbo.UI_PRINT_FORM_MESSAGE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FORM_ID | int | 4 | 0 | YES |  |  |
| MESSAGE_NAME | varchar | 50 | 0 | YES |  |  |
| TYPE_CODE | char | 4 | 1 |  |  |  |
| TITLE | nvarchar | 100 | 1 |  |  |  |
| BEEP | smallint | 2 | 1 |  |  |  |
| PICTURE_FILENAME | nvarchar | 100 | 1 |  |  |  |
| AUDIO_FILENAME | nvarchar | 100 | 1 |  |  |  |
| ACCEPT_CAPTION | nvarchar | 100 | 1 |  |  |  |
| REJECT_CAPTION | nvarchar | 100 | 1 |  |  |  |
| ABORT_CAPTION | nvarchar | 100 | 1 |  |  |  |
| TEXT_SCRIPT | nvarchar | 4000 | 1 |  |  |  |
| ACTIVE_FLG | smallint | 2 | 1 |  |  |  |

