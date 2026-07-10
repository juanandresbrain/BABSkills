# dbo.tmpAWT_DepositLoggedAsExported

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sBatchID | varchar | 50 | 0 |  |  |  |
| sDevComments | varchar | 500 | 1 |  |  |  |
| iAWTransNum | int | 4 | 0 |  |  |  |
| sOrderNumber | varchar | 50 | 0 |  |  |  |
| dTimeStamp | datetime | 8 | 0 |  |  |  |
| mAmount | money | 8 | 1 |  |  |  |
| iStoreID | int | 4 | 0 |  |  |  |
| sSiteCode | varchar | 10 | 1 |  |  |  |
