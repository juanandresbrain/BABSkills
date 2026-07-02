# dbo.SNAPSHOT_INSTANCE

**Database:** REPL_MAN  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SNAPSHOT_INSTANCE_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| SNAPSHOT_NAME | varchar | 30 | 0 |  |  |  |
| INSTANCE_NO | varchar | 20 | 1 |  |  |  |
| PHYSICAL_NAME | varchar | 50 | 0 |  |  |  |
| CREATION_DATETIME | datetime | 8 | 1 |  |  |  |
| STATUS | char | 4 | 1 |  |  |  |
| VERSION_NO | varchar | 20 | 1 |  |  |  |

