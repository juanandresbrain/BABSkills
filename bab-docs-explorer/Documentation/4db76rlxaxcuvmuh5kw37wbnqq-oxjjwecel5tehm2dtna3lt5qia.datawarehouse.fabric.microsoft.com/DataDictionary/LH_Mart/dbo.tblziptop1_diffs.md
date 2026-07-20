# dbo.tblziptop1_diffs

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| datestamp | datetime2 | 8 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| old_store_key | int | 4 | 1 |  |  |  |
| new_store_key | int | 4 | 1 |  |  |  |
| old_distance | float | 8 | 1 |  |  |  |
| new_distance | float | 8 | 1 |  |  |  |
