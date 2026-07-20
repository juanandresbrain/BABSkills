# dbo.azure_crm_transaction_key_story_ranking_purchases

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Country | varchar | 8000 | 1 |  |  |  |
| PurchaseChannel | varchar | 8000 | 1 |  |  |  |
| customerNumber | varchar | 8000 | 1 |  |  |  |
| transaction_ID | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| GaapUnits | int | 4 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isRetail | int | 4 | 1 |  |  |  |
| 2ndPurchase | varchar | 8000 | 1 |  |  |  |
| 3rdPurchase | varchar | 8000 | 1 |  |  |  |
| 4thPurchase | varchar | 8000 | 1 |  |  |  |
| isNewCustomer | int | 4 | 1 |  |  |  |
| isRepeatCustomer | int | 4 | 1 |  |  |  |
| licenseStatus | varchar | 8000 | 1 |  |  |  |
| webOrRetail | varchar | 8000 | 1 |  |  |  |
