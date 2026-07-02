# dbo.ServiceLoggingGeneralUsage

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | bigint | 8 | 0 | YES |  |  |
| LogCreatedDate | datetime | 8 | 0 |  |  |  |
| Message | nvarchar | -1 | 1 |  |  |  |
| IsAnException | bit | 1 | 0 |  |  |  |
| ExceptionMessage | nvarchar | -1 | 1 |  |  |  |
| ExceptionStacktrace | nvarchar | -1 | 1 |  |  |  |
| ServiceID | int | 4 | 1 |  | YES |  |
| FunctionName | nvarchar | 510 | 1 |  |  |  |

