# dbo.UI_KEYBOARD_KEY

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| KEYBOARD_ID | int | 4 | 0 | YES |  |  |
| KEY_ID | int | 4 | 0 | YES |  |  |
| KEY_CODE | smallint | 2 | 1 |  |  |  |
| SHIFT_STATE | smallint | 2 | 1 |  |  |  |
| SCREEN_TOP | int | 4 | 1 |  |  |  |
| SCREEN_LEFT | int | 4 | 1 |  |  |  |
| SCREEN_WIDTH | int | 4 | 1 |  |  |  |
| SCREEN_HEIGHT | int | 4 | 1 |  |  |  |
| SCREEN_BACK_COLOR | int | 4 | 1 |  |  |  |
| SCREEN_FORE_COLOR | int | 4 | 1 |  |  |  |
| KEY_NAME | nvarchar | 100 | 1 |  |  |  |

