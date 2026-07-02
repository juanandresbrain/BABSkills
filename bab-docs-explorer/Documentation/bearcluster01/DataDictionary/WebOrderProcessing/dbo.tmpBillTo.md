# dbo.tmpBillTo

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 10 | 1 |  |  |  |
| TransactionID | int | 4 | 0 |  |  |  |
| BillToFName | varchar | 50 | 1 |  |  |  |
| BillToLName | varchar | 50 | 1 |  |  |  |
| BillToAddress1 | varchar | 100 | 1 |  |  |  |
| BillToAddress2 | varchar | 100 | 0 |  |  |  |
| BillToCity | varchar | 50 | 1 |  |  |  |
| BillToState | varchar | 50 | 1 |  |  |  |
| BillToPostalCode | varchar | 20 | 1 |  |  |  |
| BillToCountry | varchar | 30 | 1 |  |  |  |
| BillToPhone | varchar | 20 | 1 |  |  |  |
| BillToEmail | varchar | 100 | 1 |  |  |  |

