# dbo.azure_crm_transaction_key_story_ranking

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Country | varchar | 8000 | 1 |  |  |  |
| PurchaseChannel | varchar | 8000 | 1 |  |  |  |
| customerNumber | varchar | 8000 | 1 |  |  |  |
| transactionID | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| keyStory | varchar | 8000 | 1 |  |  |  |
| KeyRankPerTransaction | int | 4 | 1 |  |  |  |
| KeyRankPerSequenceNewVOldCustomers | int | 4 | 1 |  |  |  |
| KeyRankPerSequenceGlobal | int | 4 | 1 |  |  |  |
| KeyStorySales | decimal | 17 | 1 |  |  |  |
| KeyStoryUnits | bigint | 8 | 1 |  |  |  |
| CustomerFirstTransactionDate | varchar | 8000 | 1 |  |  |  |
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
| hasCountYourCandles | bigint | 8 | 1 |  |  |  |
| hasBirthdayGift | bigint | 8 | 1 |  |  |  |
| hasHalfBirthday | bigint | 8 | 1 |  |  |  |
| hasWinback | bigint | 8 | 1 |  |  |  |
| hasOther | bigint | 8 | 1 |  |  |  |
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| firstPurchaseFlag | varchar | 8000 | 1 |  |  |  |
