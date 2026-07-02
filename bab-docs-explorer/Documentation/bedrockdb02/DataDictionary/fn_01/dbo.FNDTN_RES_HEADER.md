# dbo.FNDTN_RES_HEADER

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RESOURCE_ID | int | 4 | 0 | YES |  |  |
| NAMESPACE_NAME | varchar | 512 | 0 |  |  |  |
| RESOURCE_NAME | varchar | 255 | 0 |  |  |  |
| IS_USER | tinyint | 1 | 0 | YES |  |  |
| RESOURCE_TYPE | int | 4 | 0 |  |  |  |
| RESOURCE_COMMENT | nvarchar | 1024 | 1 |  |  |  |
| MESSAGE_BUTTON | tinyint | 1 | 0 |  |  |  |
| MESSAGE_ICON | tinyint | 1 | 0 |  |  |  |
| MESSAGE_BUTTON_DEFAULT | tinyint | 1 | 0 |  |  |  |
| ACTIVE_FLAG | bit | 1 | 0 |  |  |  |
| USED_BY_INFRMTN_CNTR | bit | 1 | 0 |  |  |  |

