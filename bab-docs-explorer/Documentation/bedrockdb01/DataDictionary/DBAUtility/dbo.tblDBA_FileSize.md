# dbo.tblDBA_FileSize

**Database:** DBAUtility  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Process | smallint | 2 | 1 |  |  |  |
| UserName | varchar | 100 | 1 |  |  |  |
| Directory | varchar | 400 | 1 |  |  |  |
| FilePath | varchar | 400 | 1 |  |  |  |
| SizeInMB | decimal | 9 | 1 |  |  |  |
| SizeInKB | decimal | 9 | 1 |  |  |  |
| ModifiedDate | datetime | 8 | 1 |  |  |  |
