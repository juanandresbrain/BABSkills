# dbo.tmpkeysales1

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| country | varchar | 8000 | 1 |  |  |  |
| PurchaseChannel | varchar | 8000 | 1 |  |  |  |
| customerNumber | varchar | 8000 | 1 |  |  |  |
| transactionID | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| Sales | decimal | 17 | 1 |  |  |  |
| Units | bigint | 8 | 1 |  |  |  |
| CustomerFirstTransactionDate | varchar | 8000 | 1 |  |  |  |
| isFreshCustomer | int | 4 | 1 |  |  |  |
| isFirstPurchaseChannel | int | 4 | 1 |  |  |  |
| isFirstPurchase | int | 4 | 1 |  |  |  |
| isNewCustomer | int | 4 | 1 |  |  |  |
| isRepeatCustomer | int | 4 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isRetail | int | 4 | 1 |  |  |  |
| LifetimeTransactionSequence | int | 4 | 1 |  |  |  |
| LifetimeVisitSequence | int | 4 | 1 |  |  |  |
| GaapSalesTranTotal | decimal | 17 | 1 |  |  |  |
| bonusClubMember | int | 4 | 1 |  |  |  |
| nonCrmTransFlag | int | 4 | 1 |  |  |  |
