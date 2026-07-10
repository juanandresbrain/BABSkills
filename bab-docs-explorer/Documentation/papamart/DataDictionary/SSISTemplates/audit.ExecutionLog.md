# audit.ExecutionLog

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | int | 4 | 0 | YES |  |  |
| ParentLogID | int | 4 | 1 |  |  |  |
| Description | varchar | 50 | 1 |  |  |  |
| PackageName | varchar | 50 | 0 |  |  |  |
| PackageGuid | uniqueidentifier | 16 | 0 |  |  |  |
| MachineName | varchar | 50 | 0 |  |  |  |
| ExecutionGuid | uniqueidentifier | 16 | 0 |  |  |  |
| LogicalDate | datetime | 8 | 0 |  |  |  |
| Operator | varchar | 50 | 0 |  |  |  |
| StartTime | datetime | 8 | 0 |  |  |  |
| EndTime | datetime | 8 | 1 |  |  |  |
| Status | tinyint | 1 | 0 |  |  |  |
| FailureTask | varchar | 64 | 1 |  |  |  |
