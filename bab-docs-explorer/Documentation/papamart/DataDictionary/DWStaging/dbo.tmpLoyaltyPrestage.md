# dbo.tmpLoyaltyPrestage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| TransactionLineNumber | int | 4 | 1 |  |  |  |
| DiscountReference | varchar | 80 | 1 |  |  |  |
| inDiscountFacts | bit | 1 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| TransactionYear | varchar | 20 | 1 |  |  |  |
| TransactionMonth | varchar | 20 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | nvarchar | 160 | 1 |  |  |  |
| StoreNumber | varchar | 80 | 1 |  |  |  |
| Country | varchar | 80 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| PurchaseRevenue | decimal | 5 | 1 |  |  |  |
| LineItemPrice | decimal | 5 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 5 | 1 |  |  |  |
| ParentTransactionSubTotal | decimal | 17 | 1 |  |  |  |
| ShippingUGA | decimal | 17 | 1 |  |  |  |
| ProductKey | varchar | 20 | 1 |  |  |  |
| SKU | varchar | 20 | 1 |  |  |  |
| KeyStory | nvarchar | 160 | 1 |  |  |  |
| ConsumerGroup | varchar | 80 | 1 |  |  |  |
| Department | varchar | 80 | 1 |  |  |  |
| LicensedOrNot | bit | 1 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| Class | varchar | 20 | 1 |  |  |  |
| SubClass | varchar | 20 | 1 |  |  |  |
| isPointsEligible | bit | 1 | 1 |  |  |  |
