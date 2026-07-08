# dbo.tblQueue

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| QueueID | decimal | 9 | 0 | YES |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| QueueName | varchar | 80 | 0 |  |  |  |
| FileTypeNum | int | 4 | 0 |  |  |  |
| Priority | smallint | 2 | 0 |  |  |  |
| Direction | smallint | 2 | 0 |  |  |  |
| HostDir | nvarchar | 510 | 0 |  |  |  |
| RemoteDir | nvarchar | 510 | 0 |  |  |  |
| Mask | nvarchar | 160 | 0 |  |  |  |
| EOFIndicator | int | 4 | 0 |  |  |  |
| TempExtension | nvarchar | 40 | 0 |  |  |  |
| ControlExtension | nvarchar | 40 | 0 |  |  |  |
| NumCopies | int | 4 | 0 |  |  |  |
| DestName | nvarchar | 60 | 1 |  |  |  |
| SourceMachineS | nvarchar | 100 | 1 |  |  |  |
| DestMachineD | nvarchar | 100 | 1 |  |  |  |
| DestBackups | int | 4 | 1 |  |  |  |
| QueueIDVersion | int | 4 | 0 |  |  |  |
| CreateEODFlag | int | 4 | 0 |  |  |  |
| CreateEOFFlag | int | 4 | 0 |  |  |  |
| CreateRemoteDir | int | 4 | 0 |  |  |  |
| EODPoll | int | 4 | 0 |  |  |  |
| ManualPoll | int | 4 | 0 |  |  |  |
| TricklePeriodicPoll | int | 4 | 0 |  |  |  |
| MaxTransferTime | int | 4 | 0 |  |  |  |
| CompressionUsed | int | 4 | 0 |  |  |  |
| Compression | int | 4 | 0 |  |  |  |
| SoftwareDistributionQ | int | 4 | 0 |  |  |  |
| DUE_DAY | smallint | 2 | 0 |  |  |  |
| DUE_TIME | datetime | 8 | 0 |  |  |  |
| DUE_DAY_CUT_OFF | smallint | 2 | 0 |  |  |  |
| DUE_TIME_CUT_OFF | datetime | 8 | 0 |  |  |  |
| EXPCTD_TRNSFR_SNC_OPNG | smallint | 2 | 1 |  |  |  |
