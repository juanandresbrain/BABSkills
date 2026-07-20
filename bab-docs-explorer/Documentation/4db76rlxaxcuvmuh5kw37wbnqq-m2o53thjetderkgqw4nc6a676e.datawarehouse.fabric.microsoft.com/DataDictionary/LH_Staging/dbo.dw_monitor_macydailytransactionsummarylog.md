# dbo.dw_monitor_macydailytransactionsummarylog

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MacyDailyTransactionSummaryLogID | int | 4 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| SaleDate | datetime2 | 8 | 1 |  |  |  |
| PLUAmount | decimal | 9 | 1 |  |  |  |
