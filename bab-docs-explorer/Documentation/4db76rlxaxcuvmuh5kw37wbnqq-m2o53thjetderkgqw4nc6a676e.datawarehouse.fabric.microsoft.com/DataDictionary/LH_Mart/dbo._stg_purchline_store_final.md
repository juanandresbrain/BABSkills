# dbo._stg_purchline_store_final

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| purchid | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| inventdimid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventlocation_name | varchar | 8000 | 1 |  |  |  |
| derived_store_id_A | int | 4 | 1 |  |  |  |
| store_key_A | int | 4 | 1 |  |  |  |
| store_id_A | int | 4 | 1 |  |  |  |
| store_name_A | varchar | 8000 | 1 |  |  |  |
| region_A | varchar | 8000 | 1 |  |  |  |
| postal_code_A | varchar | 8000 | 1 |  |  |  |
| A_matched | int | 4 | 1 |  |  |  |
| A_path | varchar | 8000 | 1 |  |  |  |
| ship_postal_code | varchar | 8000 | 1 |  |  |  |
| store_key_B | int | 4 | 1 |  |  |  |
| store_id_B | int | 4 | 1 |  |  |  |
| store_name_B | varchar | 8000 | 1 |  |  |  |
| region_B | varchar | 8000 | 1 |  |  |  |
| postal_code_B | varchar | 8000 | 1 |  |  |  |
| B_matched | int | 4 | 1 |  |  |  |
| B_path | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| store_name | varchar | 8000 | 1 |  |  |  |
| region | varchar | 8000 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| match_source | varchar | 8000 | 1 |  |  |  |
| matched | int | 4 | 1 |  |  |  |
| derived_store_id | int | 4 | 1 |  |  |  |
