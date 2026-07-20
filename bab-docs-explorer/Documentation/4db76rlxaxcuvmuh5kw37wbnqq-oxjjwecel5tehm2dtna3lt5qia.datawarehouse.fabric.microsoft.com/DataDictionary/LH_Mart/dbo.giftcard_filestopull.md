# dbo.giftcard_filestopull

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 1 |  |  |  |
| FTP_Server | varchar | 8000 | 1 |  |  |  |
| FTP_FileName | varchar | 8000 | 1 |  |  |  |
| MustPullFile | bit | 1 | 1 |  |  |  |
| DropDirectory | varchar | 8000 | 1 |  |  |  |
| GroupCode | varchar | 8000 | 1 |  |  |  |
| FileType | varchar | 8000 | 1 |  |  |  |
| GroupID | varchar | 8000 | 1 |  |  |  |
| HeaderTable | varchar | 8000 | 1 |  |  |  |
| HeaderGroupIDRequired | bit | 1 | 1 |  |  |  |
| DetailTable | varchar | 8000 | 1 |  |  |  |
| Active | bit | 1 | 1 |  |  |  |
| Comment | varchar | 8000 | 1 |  |  |  |
