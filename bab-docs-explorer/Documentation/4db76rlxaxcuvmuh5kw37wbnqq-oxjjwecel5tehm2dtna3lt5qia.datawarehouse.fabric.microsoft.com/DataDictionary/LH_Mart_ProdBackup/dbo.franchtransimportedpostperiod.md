# dbo.franchtransimportedpostperiod

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 8000 | 1 |  |  |  |
| TransactionID | varchar | 8000 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| ImportDate | date | 3 | 1 |  |  |  |
| PreviousPeriodCutOffDate | date | 3 | 1 |  |  |  |
| TransactionPayment | decimal | 17 | 1 |  |  |  |
| GrossSales | decimal | 17 | 1 |  |  |  |
| GiftCardAmount | decimal | 17 | 1 |  |  |  |
| OriginalGrossSales | decimal | 17 | 1 |  |  |  |
| OriginalGiftCardAmount | decimal | 17 | 1 |  |  |  |
| OriginalInsertDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| StoreID | varchar | 8000 | 1 |  |  |  |
