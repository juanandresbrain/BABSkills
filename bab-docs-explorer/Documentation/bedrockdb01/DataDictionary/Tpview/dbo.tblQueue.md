# dbo.tblQueue

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| QueueID | numeric | 9 | 0 | YES |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| QueueName | varchar | 80 | 0 |  |  |  |
| FileTypeNum | int | 4 | 0 |  |  |  |
| Priority | smallint | 2 | 0 |  |  |  |
| Direction | smallint | 2 | 0 |  |  |  |
| HostDir | varchar | 255 | 0 |  |  |  |
| RemoteDir | varchar | 255 | 0 |  |  |  |
| Mask | varchar | 80 | 0 |  |  |  |
| EOFIndicator | int | 4 | 0 |  |  |  |
| TempExtension | varchar | 20 | 0 |  |  |  |
| ControlExtension | varchar | 20 | 0 |  |  |  |
| NumCopies | int | 4 | 0 |  |  |  |
| DestName | varchar | 30 | 1 |  |  |  |
| SourceMachineS | varchar | 50 | 1 |  |  |  |
| DestMachineD | varchar | 50 | 1 |  |  |  |
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
