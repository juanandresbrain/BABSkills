# dbo.tmployaltytransactionsstage

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| TransactionLineNumber | int | 4 | 1 |  |  |  |
| DiscountReference | varchar | 8000 | 1 |  |  |  |
| inDiscountFacts | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| TransactionYear | int | 4 | 1 |  |  |  |
| TransactionMonth | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | varchar | 8000 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| Units | bigint | 8 | 1 |  |  |  |
| PurchaseRevenue | decimal | 17 | 1 |  |  |  |
| LineItemPrice | decimal | 13 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 13 | 1 |  |  |  |
| ParentTransactionSubTotal | decimal | 17 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| Class | varchar | 8000 | 1 |  |  |  |
| SubClass | varchar | 8000 | 1 |  |  |  |
| ConsumerGroup | varchar | 8000 | 1 |  |  |  |
| Department | varchar | 8000 | 1 |  |  |  |
| LicensedOrNot | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| isPointsEligible | int | 4 | 1 |  |  |  |
| OrderReference | varchar | 8000 | 1 |  |  |  |
| EmployeeID | int | 4 | 1 |  |  |  |
| matchedByEmail | bit | 1 | 1 |  |  |  |
