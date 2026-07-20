# dbo.flashgaapsalesprestage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNo | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionHour | int | 4 | 1 |  |  |  |
| NetSales | decimal | 17 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| NetUnits | int | 4 | 1 |  |  |  |
| Source | varchar | 8000 | 1 |  |  |  |
