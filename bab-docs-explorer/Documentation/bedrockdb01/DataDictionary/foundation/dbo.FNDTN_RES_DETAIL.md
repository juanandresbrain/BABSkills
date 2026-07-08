# dbo.FNDTN_RES_DETAIL

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RESOURCE_ID | int | 4 | 0 |  |  |  |
| CULTURE_LCID | int | 4 | 0 |  |  |  |
| IS_USER | tinyint | 1 | 0 |  |  |  |
| RESOURCE_VALUE | nvarchar | 4000 | 1 |  |  |  |
| RESOURCE_IMAGE | image | 16 | 1 |  |  |  |
