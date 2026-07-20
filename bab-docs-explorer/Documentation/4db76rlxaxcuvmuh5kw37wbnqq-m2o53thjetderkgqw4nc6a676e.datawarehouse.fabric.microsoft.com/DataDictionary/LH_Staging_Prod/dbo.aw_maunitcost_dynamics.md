# dbo.aw_maunitcost_dynamics

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | varchar | 8000 | 1 |  |  |  |
| store_key | varchar | 8000 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| netCost | decimal | 9 | 1 |  |  |  |
| netUnits | int | 4 | 1 |  |  |  |
| unitCost | decimal | 9 | 1 |  |  |  |
| return_units | int | 4 | 1 |  |  |  |
| prior_date_key | int | 4 | 1 |  |  |  |
