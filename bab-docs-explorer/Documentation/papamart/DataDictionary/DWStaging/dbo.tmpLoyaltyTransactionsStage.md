# dbo.tmpLoyaltyTransactionsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| TransactionLineNumber | bigint | 8 | 1 |  |  |  |
| DiscountReference | varchar | 80 | 1 |  |  |  |
| inDiscountFacts | int | 4 | 0 |  |  |  |
| CustomerNumber | varchar | 20 | 0 |  |  |  |
| TransactionYear | int | 4 | 1 |  |  |  |
| TransactionMonth | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | nvarchar | 12 | 1 |  |  |  |
| StoreNumber | varchar | 4 | 1 |  |  |  |
| Country | varchar | 50 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| PurchaseRevenue | decimal | 17 | 1 |  |  |  |
| LineItemPrice | decimal | 17 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 17 | 1 |  |  |  |
| ParentTransactionSubTotal | decimal | 17 | 1 |  |  |  |
| ProductKey | int | 4 | 0 |  |  |  |
| SKU | varchar | 255 | 1 |  |  |  |
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| Class | varchar | 20 | 1 |  |  |  |
| SubClass | varchar | 20 | 1 |  |  |  |
| ConsumerGroup | varchar | 20 | 1 |  |  |  |
| Department | varchar | 255 | 1 |  |  |  |
| LicensedOrNot | int | 4 | 0 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| isPointsEligible | int | 4 | 1 |  |  |  |
| OrderReference | varchar | 50 | 1 |  |  |  |
| EmployeeID | int | 4 | 1 |  |  |  |
| matchedByEmail | bit | 1 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
