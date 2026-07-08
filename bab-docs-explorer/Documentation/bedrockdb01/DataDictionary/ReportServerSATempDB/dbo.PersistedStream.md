# dbo.PersistedStream

**Database:** ReportServerSATempDB  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | varchar | 32 | 0 |  |  |  |
| Index | int | 4 | 0 |  |  |  |
| Content | image | 16 | 1 |  |  |  |
| Name | nvarchar | 520 | 1 |  |  |  |
| MimeType | nvarchar | 520 | 1 |  |  |  |
| Extension | nvarchar | 520 | 1 |  |  |  |
| Encoding | nvarchar | 520 | 1 |  |  |  |
| Error | nvarchar | 1024 | 1 |  |  |  |
| RefCount | int | 4 | 0 |  |  |  |
| ExpirationDate | datetime | 8 | 0 |  |  |  |
