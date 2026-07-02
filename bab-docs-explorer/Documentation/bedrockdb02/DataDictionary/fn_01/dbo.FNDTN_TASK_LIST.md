# dbo.FNDTN_TASK_LIST

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TASK_ID | numeric | 9 | 0 | YES |  |  |
| DESCRIPTION | nvarchar | 100 | 1 |  |  |  |
| CREATION_DATE | datetime | 8 | 1 |  |  |  |
| DUE_DATE | datetime | 8 | 1 |  |  |  |
| STATUS | smallint | 2 | 1 |  |  |  |
| USER_ID | numeric | 9 | 1 |  |  |  |
| USER_GROUP_ID | numeric | 9 | 1 |  |  |  |
| APPLICATION_ID | numeric | 9 | 1 |  |  |  |
| DB_GROUP_ID | numeric | 9 | 1 |  |  |  |
| WORK_AREA | nvarchar | 200 | 1 |  |  |  |
| UPDATESTAMP | datetime | 8 | 1 |  |  |  |
| CREATED_BY_USER_ID | numeric | 9 | 0 |  |  |  |
| PROD_ID | nvarchar | 60 | 0 |  |  |  |
| USER_DATA | ntext | 16 | 1 |  |  |  |
| GUID | uniqueidentifier | 16 | 1 |  |  |  |
| MODULE_TYPE_NAME | varchar | 50 | 1 |  |  |  |
| CATEGORY_CODE | smallint | 2 | 1 |  |  |  |
| NEXT_TASK_ID | numeric | 9 | 1 |  |  |  |
| PRIORITY | smallint | 2 | 1 |  |  |  |

