# dbo.SESSION_CONTEXT

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SESSION_ID | varchar | 50 | 0 | YES |  |  |
| CONTEXT_NAME | varchar | 50 | 0 | YES |  |  |
| LAST_UPDATED | datetime | 8 | 1 |  |  |  |
| CONTEXT_DATA | image | 16 | 1 |  |  |  |

