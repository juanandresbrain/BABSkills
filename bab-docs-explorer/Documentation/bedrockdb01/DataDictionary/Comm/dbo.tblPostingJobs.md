# dbo.tblPostingJobs

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PostingJobID | int | 4 | 0 | YES |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| Name | varchar | 50 | 0 |  |  |  |
| JobType | int | 4 | 0 |  |  |  |
| MoveType | int | 4 | 0 |  |  |  |
| SendTimer | int | 4 | 1 |  |  |  |
| HostNameS | nvarchar | 40 | 1 |  |  |  |
| SourceDirectoryS | nvarchar | 160 | 1 |  |  |  |
| TempDirectoryS | nvarchar | 100 | 1 |  |  |  |
| UserNameS | nvarchar | 128 | 0 |  |  |  |
| PasswordS | nvarchar | 322 | 0 |  |  |  |
| CutOff | datetime | 8 | 1 |  |  |  |
| Mask | nvarchar | 160 | 0 |  |  |  |
| CreateDir | int | 4 | 1 |  |  |  |
| XFerExtension | nvarchar | 20 | 1 |  |  |  |
| CtlFile | int | 4 | 1 |  |  |  |
| DestinationDirD | nvarchar | 160 | 1 |  |  |  |
| SourceBackupsS | int | 4 | 1 |  |  |  |
| TempBackupsS | int | 4 | 1 |  |  |  |
| ReitmansPDTStyle | int | 4 | 1 |  |  |  |
| DestFileNameD | nvarchar | 160 | 1 |  |  |  |
| SplitFileMode | int | 4 | 1 |  |  |  |
| AddLFAfterCR | int | 4 | 1 |  |  |  |
| HostNameD | nvarchar | 40 | 1 |  |  |  |
| UserNameD | nvarchar | 128 | 0 |  |  |  |
| PasswordD | nvarchar | 322 | 0 |  |  |  |
| TempDirD | nvarchar | 100 | 1 |  |  |  |
| TempBackupsD | int | 4 | 1 |  |  |  |
| DontUseCutOff | int | 4 | 1 |  |  |  |
| SourceMachineS | nvarchar | 100 | 1 |  |  |  |
| DestMachineD | nvarchar | 100 | 1 |  |  |  |
| DeleteSource | int | 4 | 1 |  |  |  |
| RemoveCR | int | 4 | 1 |  |  |  |
| POSSoftware | int | 4 | 0 |  |  |  |
| PostingJobIDVersion | int | 4 | 0 |  |  |  |
| CompressionUsed | int | 4 | 0 |  |  |  |
| DUE_DAY | smallint | 2 | 0 |  |  |  |
| DUE_TIME | datetime | 8 | 0 |  |  |  |
| DUE_DAY_CUT_OFF | smallint | 2 | 0 |  |  |  |
| DUE_TIME_CUT_OFF | datetime | 8 | 0 |  |  |  |
| SNGL_OTPT_FILE | smallint | 2 | 0 |  |  |  |
| KEEP_SRC_FLNM | tinyint | 1 | 0 |  |  |  |
