# dbo.UI_USER_MESSAGE

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CATEGORY_NAME | varchar | 50 | 0 | YES |  |  |
| FLOW_ID | int | 4 | 0 | YES |  |  |
| USER_MESSAGE_NAME | varchar | 50 | 0 | YES |  |  |
| USER_MESSAGE_TYPE_CODE | char | 4 | 1 |  |  |  |
| TITLE | nvarchar | 100 | 1 |  |  |  |
| TEXT_SCRIPT | nvarchar | 4000 | 1 |  |  |  |
| BEEP | smallint | 2 | 1 |  |  |  |
| PICTURE_FILENAME | nvarchar | 100 | 1 |  |  |  |
| AUDIO_FILENAME | nvarchar | 100 | 1 |  |  |  |
| ACCEPT_CAPTION | nvarchar | 100 | 1 |  |  |  |
| REJECT_CAPTION | nvarchar | 100 | 1 |  |  |  |
| ABORT_CAPTION | nvarchar | 100 | 1 |  |  |  |
| BEEP_REPEAT | smallint | 2 | 1 |  |  |  |
| BEEP_DELAY | int | 4 | 1 |  |  |  |
| BEEP_REPEAT_DELAY | int | 4 | 1 |  |  |  |
| AUDIO_REPEAT | smallint | 2 | 1 |  |  |  |
| AUDIO_DELAY | int | 4 | 1 |  |  |  |
| AUDIO_REPEAT_DELAY | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

