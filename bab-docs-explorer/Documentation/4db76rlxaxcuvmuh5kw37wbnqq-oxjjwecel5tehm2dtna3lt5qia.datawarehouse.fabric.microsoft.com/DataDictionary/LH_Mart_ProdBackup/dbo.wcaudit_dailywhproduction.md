# dbo.wcaudit_dailywhproduction

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DateOf | datetime2 | 8 | 1 |  |  |  |
| inQueue | int | 4 | 1 |  |  |  |
| inQueueValue | decimal | 9 | 1 |  |  |  |
| shipped | int | 4 | 1 |  |  |  |
| shippedValue | decimal | 9 | 1 |  |  |  |
| inQueueLastYear | int | 4 | 1 |  |  |  |
| inQueueValueLastYear | decimal | 9 | 1 |  |  |  |
| shippedLastYear | int | 4 | 1 |  |  |  |
| shippedValueLastYear | decimal | 9 | 1 |  |  |  |
