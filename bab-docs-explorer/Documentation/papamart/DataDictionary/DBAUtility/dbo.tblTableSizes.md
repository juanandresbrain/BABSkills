# dbo.tblTableSizes

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TableEntryID | int | 4 | 0 | YES |  |  |
| EntryDate | smalldatetime | 4 | 0 |  |  |  |
| TableName | varchar | 200 | 1 |  |  |  |
| Row_Count | int | 4 | 1 |  |  |  |
| ReservedSize | varchar | 20 | 1 |  |  |  |
| DataSize | varchar | 20 | 1 |  |  |  |
| IndexSize | varchar | 20 | 1 |  |  |  |
| UnusedSize | varchar | 20 | 1 |  |  |  |
| CreationDate | smalldatetime | 4 | 1 |  |  |  |
