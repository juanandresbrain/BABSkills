# dbo.tmpAWTFileMovement

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sBatchID | varchar | 50 | 0 |  |  |  |
| dTimeStamp | datetime2 | 8 | 0 |  |  |  |
| bSentToAW | bit | 1 | 1 |  |  |  |
| sDevComments | varchar | 500 | 1 |  |  |  |
| sCreatedBy | varchar | 50 | 0 |  |  |  |
| firstdate | smalldatetime | 4 | 1 |  |  |  |
| lastdate | smalldatetime | 4 | 1 |  |  |  |
