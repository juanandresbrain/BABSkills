# dbo.tblJobTransfer

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobTransferID | int | 4 | 0 | YES |  |  |
| SrcMachineID | int | 4 | 0 |  |  |  |
| SrcDir | nvarchar | 510 | 0 |  |  |  |
| SrcFile | nvarchar | 100 | 0 |  |  |  |
| SrcBackup | int | 4 | 0 |  |  |  |
| SrcType | int | 4 | 0 |  |  |  |
| DstMachineID | int | 4 | 0 |  |  |  |
| DstDir | nvarchar | 510 | 0 |  |  |  |
| DstFile | nvarchar | 100 | 0 |  |  |  |
| DstType | int | 4 | 0 |  |  |  |
| SrcDelete | int | 4 | 0 |  |  |  |
| DstOverwrite | int | 4 | 0 |  |  |  |
| TransferMode | int | 4 | 0 |  |  |  |
| SourceFilenameFormat | int | 4 | 0 |  |  |  |
| SourceFilenameDetails | nvarchar | 100 | 0 |  |  |  |
| DestFilenameFormat | int | 4 | 0 |  |  |  |
| DestFilenameDetails | nvarchar | 100 | 0 |  |  |  |
| RemoteRenameAfterTrans | int | 4 | 0 |  |  |  |
| RemoteRenameType | int | 4 | 0 |  |  |  |
| RemoteRenameExtension | nvarchar | 40 | 0 |  |  |  |
| AfterTransDelay | int | 4 | 0 |  |  |  |
| SDM_SRC_FILE_TYPE | int | 4 | 0 |  |  |  |
| SDM_TKN_FRMTNG_TYPE | int | 4 | 0 |  |  |  |
| SDM_TKN_LEN | int | 4 | 0 |  |  |  |
| SDM_TKN_JSTFCTN_TYPE | int | 4 | 0 |  |  |  |
| SDM_TKN_PDNG_CHRCTR | int | 4 | 0 |  |  |  |
