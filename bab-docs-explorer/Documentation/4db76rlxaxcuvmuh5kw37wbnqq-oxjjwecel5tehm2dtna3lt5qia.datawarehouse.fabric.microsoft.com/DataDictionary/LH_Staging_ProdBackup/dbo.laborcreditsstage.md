# dbo.laborcreditsstage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DateSubmitted | date | 3 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| Month | varchar | 8000 | 1 |  |  |  |
| WeekNumber | int | 4 | 1 |  |  |  |
| Credit | decimal | 17 | 1 |  |  |  |
| Reason | varchar | 8000 | 1 |  |  |  |
| RequestedBy | varchar | 8000 | 1 |  |  |  |
