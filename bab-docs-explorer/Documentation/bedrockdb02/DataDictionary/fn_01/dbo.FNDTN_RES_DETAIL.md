# dbo.FNDTN_RES_DETAIL

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RESOURCE_ID | int | 4 | 0 | YES |  |  |
| CULTURE_LCID | int | 4 | 0 | YES |  |  |
| IS_USER | tinyint | 1 | 0 | YES |  |  |
| RESOURCE_VALUE | nvarchar | 4000 | 1 |  |  |  |
| RESOURCE_IMAGE | image | 16 | 1 |  |  |  |

