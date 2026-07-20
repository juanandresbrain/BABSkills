# dbo.tmpbcvisit2

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Country | varchar | 8000 | 1 |  |  |  |
| PurchaseChannel | varchar | 8000 | 1 |  |  |  |
| customerNumber | varchar | 8000 | 1 |  |  |  |
| transactionID | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| keyStory | varchar | 8000 | 1 |  |  |  |
| KeyRankPerTransaction | bigint | 8 | 1 |  |  |  |
| KeyRankPerSequenceNewVOldCustomers | bigint | 8 | 1 |  |  |  |
| KeyRankPerSequenceGlobal | bigint | 8 | 1 |  |  |  |
| KeyStorySales | decimal | 17 | 1 |  |  |  |
| KeyStoryUnits | int | 4 | 1 |  |  |  |
| CustomerFirstTransactionDate | datetime2 | 8 | 1 |  |  |  |
| isFreshCustomer | int | 4 | 1 |  |  |  |
| isFirstPurchaseChannel | int | 4 | 1 |  |  |  |
| isFirstPurchase | int | 4 | 1 |  |  |  |
| isNewCustomer | int | 4 | 1 |  |  |  |
| isRepeatCustomer | int | 4 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isRetail | int | 4 | 1 |  |  |  |
| GaapSalesTranTotal | decimal | 17 | 1 |  |  |  |
| KeyStoryPctToTotal | varchar | 8000 | 1 |  |  |  |
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
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| firstPurchaseFlag | varchar | 8000 | 1 |  |  |  |
