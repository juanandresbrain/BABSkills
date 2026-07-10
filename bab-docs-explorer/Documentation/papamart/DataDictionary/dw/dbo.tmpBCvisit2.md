# dbo.tmpBCvisit2

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Country | varchar | 50 | 1 |  |  |  |
| PurchaseChannel | nvarchar | 40 | 1 |  |  |  |
| customerNumber | varchar | 20 | 1 |  |  |  |
| transactionID | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| keyStory | nvarchar | 60 | 1 |  |  |  |
| KeyRankPerTransaction | bigint | 8 | 1 |  |  |  |
| KeyRankPerSequenceNewVOldCustomers | bigint | 8 | 1 |  |  |  |
| KeyRankPerSequenceGlobal | bigint | 8 | 1 |  |  |  |
| KeyStorySales | numeric | 17 | 1 |  |  |  |
| KeyStoryUnits | int | 4 | 1 |  |  |  |
| CustomerFirstTransactionDate | datetime | 8 | 1 |  |  |  |
| isFreshCustomer | int | 4 | 1 |  |  |  |
| isFirstPurchaseChannel | int | 4 | 1 |  |  |  |
| isFirstPurchase | int | 4 | 1 |  |  |  |
| isNewCustomer | int | 4 | 1 |  |  |  |
| isRepeatCustomer | int | 4 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isRetail | int | 4 | 1 |  |  |  |
| GaapSalesTranTotal | numeric | 17 | 1 |  |  |  |
| KeyStoryPctToTotal | varchar | 31 | 1 |  |  |  |
| LifetimeTransactionSequence | int | 4 | 1 |  |  |  |
| LifetimeVisitSequence | int | 4 | 1 |  |  |  |
| ParentTransactionID | int | 4 | 1 |  |  |  |
| ChildTransactionID | int | 4 | 1 |  |  |  |
| isTopKeyStoryPerTransaction | int | 4 | 1 |  |  |  |
| isTopKeyStoryNewOrOldGlobal | int | 4 | 1 |  |  |  |
| isTopKeyStoryGlobal | int | 4 | 1 |  |  |  |
| hasCountYourCandles | int | 4 | 1 |  |  |  |
| hasBirthdayGift | int | 4 | 1 |  |  |  |
| hasHalfBirthday | int | 4 | 1 |  |  |  |
| hasWinback | int | 4 | 1 |  |  |  |
| hasOther | int | 4 | 1 |  |  |  |
| TransactionKey | varchar | 30 | 1 |  |  |  |
| firstPurchaseFlag | varchar | 16 | 0 |  |  |  |
