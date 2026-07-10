# dbo.INTEGRITY_HIST

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SERVER_NM | nvarchar | 256 | 1 |  |  |  |
| ERR | int | 4 | 1 |  |  |  |
| ERR_LEVEL | int | 4 | 1 |  |  |  |
| DB_STATE | int | 4 | 1 |  |  |  |
| MESSAGE_TXT | nvarchar | 2048 | 1 |  |  |  |
| REPAIR_LEVEL | int | 4 | 1 |  |  |  |
| DB_STATUS | int | 4 | 1 |  |  |  |
| SERVER_DB_ID | int | 4 | 1 |  |  |  |
| DB_OBJECT_ID | int | 4 | 1 |  |  |  |
| INDEX_ID | int | 4 | 1 |  |  |  |
| PARTITION_ID | bigint | 8 | 1 |  |  |  |
| ALLOC_UNIT_ID | bigint | 8 | 1 |  |  |  |
| DB_FILE | int | 4 | 1 |  |  |  |
| PAGE | int | 4 | 1 |  |  |  |
| SLOT | int | 4 | 1 |  |  |  |
| REF_FILE | int | 4 | 1 |  |  |  |
| REF_PAGE | int | 4 | 1 |  |  |  |
| REF_SLOT | int | 4 | 1 |  |  |  |
| ALLOCATION | int | 4 | 1 |  |  |  |
| INSERT_DT | datetime | 8 | 0 |  |  |  |
