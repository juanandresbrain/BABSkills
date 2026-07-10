# dbo.GiftCard_FilesToPull

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| FTP_Server | varchar | 20 | 1 |  |  |  |
| FTP_FileName | varchar | 50 | 1 |  |  |  |
| MustPullFile | bit | 1 | 1 |  |  |  |
| DropDirectory | varchar | 75 | 1 |  |  |  |
| GroupCode | varchar | 20 | 1 |  |  |  |
| FileType | varchar | 20 | 1 |  |  |  |
| GroupID | varchar | 20 | 1 |  |  |  |
| HeaderTable | varchar | 40 | 1 |  |  |  |
| HeaderGroupIDRequired | bit | 1 | 1 |  |  |  |
| DetailTable | varchar | 40 | 1 |  |  |  |
| Active | bit | 1 | 1 |  |  |  |
| Comment | varchar | 80 | 1 |  |  |  |
