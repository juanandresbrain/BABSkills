# dbo.payroll

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| actual | decimal | 5 | 1 |  |  |  |
| earned | decimal | 5 | 1 |  |  |  |
| loaded_date | datetime2 | 8 | 1 |  |  |  |
| updated_date | datetime2 | 8 | 1 |  |  |  |
