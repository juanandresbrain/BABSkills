# dbo.tmpkeyrank

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
| sales | decimal | 17 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| CustomerFirstTransactionDate | datetime2 | 8 | 1 |  |  |  |
| isFreshCustomer | int | 4 | 1 |  |  |  |
| isFirstPurchaseChannel | int | 4 | 1 |  |  |  |
| isFirstPurchase | int | 4 | 1 |  |  |  |
| isNewCustomer | int | 4 | 1 |  |  |  |
| isRepeatCustomer | int | 4 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isRetail | int | 4 | 1 |  |  |  |
| GaapSalesTranTotal | decimal | 17 | 1 |  |  |  |
| LifetimeTransactionSequence | int | 4 | 1 |  |  |  |
| LifetimeVisitSequence | int | 4 | 1 |  |  |  |
| ParentTransactionID | int | 4 | 1 |  |  |  |
| ChildTransactionID | int | 4 | 1 |  |  |  |
