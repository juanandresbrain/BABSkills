# dbo.laborcredits

**Database:** LH_Mart  
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
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
