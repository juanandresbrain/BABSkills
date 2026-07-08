# dbo.tblJobFlow

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobFlowID | int | 4 | 0 | YES |  |  |
| JobID | int | 4 | 0 |  |  |  |
| SeqNo | int | 4 | 0 |  |  |  |
| Verb | int | 4 | 0 |  |  |  |
| JobTransferID | int | 4 | 0 |  |  |  |
| NbrRetries | int | 4 | 0 |  |  |  |
| FirstDelay | int | 4 | 0 |  |  |  |
| OtherDelay | int | 4 | 0 |  |  |  |
| StatusType | int | 4 | 0 |  |  |  |
| StatusMachineID | int | 4 | 0 |  |  |  |
| StatusDir | nvarchar | 510 | 0 |  |  |  |
| StatusFile | nvarchar | 100 | 0 |  |  |  |
| StatusSend | int | 4 | 0 |  |  |  |
