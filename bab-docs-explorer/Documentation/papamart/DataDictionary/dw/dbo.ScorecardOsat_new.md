# dbo.ScorecardOsat_new

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| Store_Key | int | 4 | 1 |  |  |  |
| Bearritory | varchar | 255 | 1 |  |  |  |
| Region | varchar | 255 | 1 |  |  |  |
| Period_Id | int | 4 | 1 |  |  |  |
| Month | varchar | 255 | 1 |  |  |  |
| RollingOSAT | decimal | 9 | 1 |  |  |  |
| RollingResponses | int | 4 | 1 |  |  |  |
| RollingScores | int | 4 | 1 |  |  |  |
| OSAT | decimal | 9 | 1 |  |  |  |
| Responses | int | 4 | 1 |  |  |  |
| Scores | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| RefreshDate | datetime | 8 | 1 |  |  |  |
