# dbo.DRIVE_HIST

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SERVER_NM | nvarchar | 256 | 1 |  |  |  |
| DRIVE | char | 1 | 1 |  |  |  |
| FREESPACE | int | 4 | 1 |  |  |  |
| TOTALSIZE | int | 4 | 1 |  |  |  |
| PERCENTFREE | int | 4 | 1 |  |  |  |
| EXECUTION_TM | datetime | 8 | 1 |  |  |  |
| EMAILSENT | bit | 1 | 1 |  |  |  |
