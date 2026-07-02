# dbo.tmpWebSalesForPOSReturns

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| OMSTransactionType | varchar | 255 | 1 |  |  |  |
| PaymentMethod | varchar | 50 | 1 |  |  |  |
| Tax | decimal | 5 | 1 |  |  |  |
| SubTotal | money | 8 | 0 |  |  |  |
| Shipping | money | 8 | 0 |  |  |  |
| TotalCharges | money | 8 | 0 |  |  |  |
| TransactionAmount | money | 8 | 0 |  |  |  |

