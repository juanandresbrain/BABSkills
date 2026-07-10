# dbo.store_dim_snapshot_uk

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| datestamp | datetime | 8 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| bearea | varchar | 100 | 1 |  |  |  |
| store_name | varchar | 255 | 1 |  |  |  |
| store_name_abbrv | varchar | 100 | 1 |  |  |  |
| bearritory | varchar | 100 | 1 |  |  |  |
| address1 | varchar | 255 | 1 |  |  |  |
| region | varchar | 100 | 1 |  |  |  |
| zone | varchar | 50 | 1 |  |  |  |
| address2 | varchar | 255 | 1 |  |  |  |
| state_province_name | varchar | 255 | 1 |  |  |  |
| business_type | varchar | 50 | 1 |  |  |  |
| city | varchar | 50 | 1 |  |  |  |
| division | varchar | 50 | 1 |  |  |  |
| state_province | varchar | 10 | 1 |  |  |  |
| county | varchar | 50 | 1 |  |  |  |
| business_unit | varchar | 50 | 1 |  |  |  |
| country | varchar | 50 | 1 |  |  |  |
| country_name | varchar | 50 | 1 |  |  |  |
| postal_code | varchar | 50 | 1 |  |  |  |
| phone | varchar | 100 | 1 |  |  |  |
| fax | varchar | 255 | 1 |  |  |  |
| email | varchar | 255 | 1 |  |  |  |
| opening_date | datetime | 8 | 1 |  |  |  |
| active | varchar | 50 | 1 |  |  |  |
| latitude | numeric | 9 | 1 |  |  |  |
| longitude | numeric | 9 | 1 |  |  |  |
| volume_group | varchar | 1 | 1 |  |  |  |
| store_mgr | varchar | 50 | 1 |  |  |  |
| bearea_mgr | varchar | 50 | 1 |  |  |  |
| bearitory_mgr | varchar | 50 | 1 |  |  |  |
| region_mgr | varchar | 50 | 1 |  |  |  |
| store_type | varchar | 50 | 1 |  |  |  |
| closing_date | datetime | 8 | 1 |  |  |  |
| comp_date | datetime | 8 | 1 |  |  |  |
| store_group_id | int | 4 | 1 |  |  |  |
| address3 | varchar | 50 | 1 |  |  |  |
| address4 | varchar | 50 | 1 |  |  |  |
| square_feet | int | 4 | 1 |  |  |  |
| num_of_pos | int | 4 | 1 |  |  |  |
| num_of_kiosks | int | 4 | 1 |  |  |  |
| postal_plus4 | char | 4 | 1 |  |  |  |
| Abbreviation | varchar | 3 | 1 |  |  |  |
| Legal_Description | varchar | 50 | 1 |  |  |  |
| comp_week_id | int | 4 | 1 |  |  |  |
| bearea_id | int | 4 | 1 |  |  |  |
| bearitory_id | int | 4 | 1 |  |  |  |
| region_id | int | 4 | 1 |  |  |  |
| division_code | char | 5 | 1 |  |  |  |
| language | varchar | 20 | 1 |  |  |  |
| demographics_bg_key | varchar | 20 | 1 |  |  |  |
