# dbo.flashgaapsalesprestage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
