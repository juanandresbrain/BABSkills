# audit.SSISLog

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventID | int | 4 | 0 | YES |  |  |
| EventType | varchar | 20 | 0 |  |  |  |
| PackageName | varchar | 50 | 0 |  |  |  |
| TaskName | varchar | 50 | 0 |  |  |  |
| EventCode | int | 4 | 1 |  |  |  |
| EventDescription | varchar | 1000 | 1 |  |  |  |
| PackageDuration | int | 4 | 1 |  |  |  |
| ContainerDuration | int | 4 | 1 |  |  |  |
| SourceCount | int | 4 | 1 |  |  |  |
| InsertCount | int | 4 | 1 |  |  |  |
| UpdateCount | int | 4 | 1 |  |  |  |
| DeleteCount | int | 4 | 1 |  |  |  |
| ExceptionCount | int | 4 | 1 |  |  |  |
| Host | varchar | 50 | 1 |  |  |  |
| LogID | int | 4 | 1 |  |  |  |
| ParentLogID | int | 4 | 1 |  |  |  |
| DuplicateCount | int | 4 | 1 |  |  |  |
| ExistingCount | int | 4 | 1 |  |  |  |
| RejectCount | int | 4 | 1 |  |  |  |
