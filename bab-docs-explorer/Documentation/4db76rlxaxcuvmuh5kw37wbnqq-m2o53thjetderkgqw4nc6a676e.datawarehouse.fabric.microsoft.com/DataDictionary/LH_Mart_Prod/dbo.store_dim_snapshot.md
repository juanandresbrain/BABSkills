# dbo.store_dim_snapshot

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| opening_date | datetime2 | 8 | 1 |  |  |  |
| closing_date | datetime2 | 8 | 1 |  |  |  |
| latitude | decimal | 9 | 1 |  |  |  |
| longitude | decimal | 9 | 1 |  |  |  |
