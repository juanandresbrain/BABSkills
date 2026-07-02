# dbo.tmpFGW

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| TransactionDate | datetime | 8 | 0 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| FulfillmentLocation | varchar | 4 | 1 |  |  |  |
| FulfillmentLocationName | varchar | 15 | 1 |  |  |  |
| TransactionType | varchar | 50 | 1 |  |  |  |
| Tax | decimal | 17 | 1 |  |  |  |
| TransactionAmount | money | 8 | 1 |  |  |  |
| UnitAmount | int | 4 | 1 |  |  |  |
| FlashGaapSales | decimal | 17 | 1 |  |  |  |
| isBOSISorBOPIS | int | 4 | 0 |  |  |  |
| ReturnsRegister | int | 4 | 0 |  |  |  |

