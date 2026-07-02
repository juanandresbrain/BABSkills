# dbo.tblDepriatedCalls

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RowNumber | int | 4 | 0 | YES |  |  |
| EventClass | int | 4 | 1 |  |  |  |
| ApplicationName | nvarchar | 256 | 1 |  |  |  |
| ClientProcessID | int | 4 | 1 |  |  |  |
| DatabaseID | int | 4 | 1 |  |  |  |
| DatabaseName | nvarchar | 256 | 1 |  |  |  |
| EventSequence | bigint | 8 | 1 |  |  |  |
| HostName | nvarchar | 256 | 1 |  |  |  |
| IntegerData2 | int | 4 | 1 |  |  |  |
| IsSystem | int | 4 | 1 |  |  |  |
| LoginName | nvarchar | 256 | 1 |  |  |  |
| LoginSid | image | 16 | 1 |  |  |  |
| NTDomainName | nvarchar | 256 | 1 |  |  |  |
| NTUserName | nvarchar | 256 | 1 |  |  |  |
| Offset | int | 4 | 1 |  |  |  |
| RequestID | int | 4 | 1 |  |  |  |
| SPID | int | 4 | 1 |  |  |  |
| ServerName | nvarchar | 256 | 1 |  |  |  |
| SessionLoginName | nvarchar | 256 | 1 |  |  |  |
| SqlHandle | image | 16 | 1 |  |  |  |
| StartTime | datetime | 8 | 1 |  |  |  |
| TextData | ntext | 16 | 1 |  |  |  |
| TransactionID | bigint | 8 | 1 |  |  |  |
| XactSequence | bigint | 8 | 1 |  |  |  |
| BinaryData | image | 16 | 1 |  |  |  |

