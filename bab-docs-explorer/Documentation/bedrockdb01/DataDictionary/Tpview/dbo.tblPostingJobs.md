# dbo.tblPostingJobs

**Database:** Tpview  
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
| HostNameS | varchar | 20 | 1 |  |  |  |
| SourceDirectoryS | varchar | 80 | 1 |  |  |  |
| TempDirectoryS | varchar | 50 | 1 |  |  |  |
| UserNameS | varchar | 20 | 1 |  |  |  |
| PasswordS | varchar | 40 | 0 |  |  |  |
| CutOff | datetime | 8 | 1 |  |  |  |
| Mask | varchar | 80 | 1 |  |  |  |
| CreateDir | int | 4 | 1 |  |  |  |
| XFerExtension | varchar | 10 | 1 |  |  |  |
| CtlFile | int | 4 | 1 |  |  |  |
| DestinationDirD | varchar | 80 | 1 |  |  |  |
| SourceBackupsS | int | 4 | 1 |  |  |  |
| TempBackupsS | int | 4 | 1 |  |  |  |
| ReitmansPDTStyle | int | 4 | 1 |  |  |  |
| DestFileNameD | varchar | 80 | 1 |  |  |  |
| SplitFileMode | int | 4 | 1 |  |  |  |
| AddLFAfterCR | int | 4 | 1 |  |  |  |
| HostNameD | varchar | 20 | 1 |  |  |  |
| UserNameD | varchar | 20 | 1 |  |  |  |
| PasswordD | varchar | 40 | 0 |  |  |  |
| TempDirD | varchar | 50 | 1 |  |  |  |
| TempBackupsD | int | 4 | 1 |  |  |  |
| DontUseCutOff | int | 4 | 1 |  |  |  |
| SourceMachineS | varchar | 50 | 1 |  |  |  |
| DestMachineD | varchar | 50 | 1 |  |  |  |
| DeleteSource | int | 4 | 1 |  |  |  |
| RemoveCR | int | 4 | 1 |  |  |  |
| POSSoftware | int | 4 | 0 |  |  |  |
| PostingJobIDVersion | int | 4 | 0 |  |  |  |
| CompressionUsed | int | 4 | 0 |  |  |  |
