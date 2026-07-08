# dbo.tblJobStatusRequestFile

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobStatusRequestFileID | int | 4 | 0 | YES |  |  |
| JobStatusRequestID | int | 4 | 0 |  |  |  |
| Name | varchar | 50 | 0 |  |  |  |
| Size | int | 4 | 0 |  |  |  |
| JobTransferID | int | 4 | 0 |  |  |  |
| DestFilename | varchar | 50 | 0 |  |  |  |
| DestFileSize | int | 4 | 0 |  |  |  |
| Direction | int | 4 | 0 |  |  |  |
| TransferMode | int | 4 | 0 |  |  |  |
