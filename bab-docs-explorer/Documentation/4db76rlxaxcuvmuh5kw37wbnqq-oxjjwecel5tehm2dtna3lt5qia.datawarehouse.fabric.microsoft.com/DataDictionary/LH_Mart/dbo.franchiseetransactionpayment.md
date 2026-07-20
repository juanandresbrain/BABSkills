# dbo.franchiseetransactionpayment

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FranchiseeTransactionHeaderID | int | 4 | 1 |  |  |  |
| FranchiseeTransactionPaymentID | int | 4 | 1 |  |  |  |
| PaymentType | varchar | 8000 | 1 |  |  |  |
| Amount | decimal | 5 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
