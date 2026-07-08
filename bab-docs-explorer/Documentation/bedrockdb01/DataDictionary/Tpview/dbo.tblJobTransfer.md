# dbo.tblJobTransfer

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobTransferID | int | 4 | 0 | YES |  |  |
| SrcMachineID | int | 4 | 0 |  |  |  |
| SrcDir | varchar | 255 | 0 |  |  |  |
| SrcFile | varchar | 50 | 0 |  |  |  |
| SrcBackup | int | 4 | 0 |  |  |  |
| SrcType | int | 4 | 0 |  |  |  |
| DstMachineID | int | 4 | 0 |  |  |  |
| DstDir | varchar | 255 | 0 |  |  |  |
| DstFile | varchar | 50 | 0 |  |  |  |
| DstType | int | 4 | 0 |  |  |  |
| SrcDelete | int | 4 | 0 |  |  |  |
| DstOverwrite | int | 4 | 0 |  |  |  |
| TransferMode | int | 4 | 0 |  |  |  |
| SourceFilenameFormat | int | 4 | 0 |  |  |  |
| SourceFilenameDetails | varchar | 50 | 0 |  |  |  |
| DestFilenameFormat | int | 4 | 0 |  |  |  |
| DestFilenameDetails | varchar | 50 | 0 |  |  |  |
| RemoteRenameAfterTrans | int | 4 | 0 |  |  |  |
| RemoteRenameType | int | 4 | 0 |  |  |  |
| RemoteRenameExtension | varchar | 20 | 0 |  |  |  |
| AfterTransDelay | int | 4 | 0 |  |  |  |
