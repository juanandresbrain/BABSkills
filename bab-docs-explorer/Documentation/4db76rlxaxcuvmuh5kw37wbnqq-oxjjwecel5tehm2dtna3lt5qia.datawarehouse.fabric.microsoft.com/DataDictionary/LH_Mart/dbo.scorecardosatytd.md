# dbo.scorecardosatytd

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store_Id | int | 4 | 1 |  |  |  |
| Store_Key | int | 4 | 1 |  |  |  |
| Bearritory | varchar | 8000 | 1 |  |  |  |
| Region | varchar | 8000 | 1 |  |  |  |
| Period_Id | int | 4 | 1 |  |  |  |
| Month | varchar | 8000 | 1 |  |  |  |
| RollingOSAT | decimal | 9 | 1 |  |  |  |
| RollingResponses | int | 4 | 1 |  |  |  |
| RollingScores | int | 4 | 1 |  |  |  |
| OSAT | decimal | 9 | 1 |  |  |  |
| Responses | int | 4 | 1 |  |  |  |
| Scores | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| RefreshDate | datetime2 | 8 | 1 |  |  |  |
