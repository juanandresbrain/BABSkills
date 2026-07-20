# dbo.week_facts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| actual | decimal | 5 | 1 |  |  |  |
| earned | decimal | 5 | 1 |  |  |  |
| loaded_date | datetime2 | 8 | 1 |  |  |  |
| updated_date | datetime2 | 8 | 1 |  |  |  |
