# dbo.tmployaltyprestage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| TransactionLineNumber | int | 4 | 1 |  |  |  |
| DiscountReference | varchar | 8000 | 1 |  |  |  |
| inDiscountFacts | bit | 1 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| TransactionYear | varchar | 8000 | 1 |  |  |  |
| TransactionMonth | varchar | 8000 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | varchar | 8000 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| PurchaseRevenue | decimal | 5 | 1 |  |  |  |
| LineItemPrice | decimal | 5 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 5 | 1 |  |  |  |
| ParentTransactionSubTotal | decimal | 17 | 1 |  |  |  |
| ShippingUGA | decimal | 17 | 1 |  |  |  |
| ProductKey | varchar | 8000 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| ConsumerGroup | varchar | 8000 | 1 |  |  |  |
| Department | varchar | 8000 | 1 |  |  |  |
| LicensedOrNot | bit | 1 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| Class | varchar | 8000 | 1 |  |  |  |
| SubClass | varchar | 8000 | 1 |  |  |  |
| isPointsEligible | bit | 1 | 1 |  |  |  |
