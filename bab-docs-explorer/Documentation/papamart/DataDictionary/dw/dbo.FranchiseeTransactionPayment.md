# dbo.FranchiseeTransactionPayment

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FranchiseeTransactionHeaderID | int | 4 | 0 |  |  |  |
| FranchiseeTransactionPaymentID | int | 4 | 0 |  |  |  |
| PaymentType | varchar | 20 | 0 |  |  |  |
| Amount | numeric | 5 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| BatchID | varchar | 52 | 0 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
