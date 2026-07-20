# dbo.ds_geo

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| geography_sk | bigint | 8 | 1 |  |  |  |
| country_code | varchar | 2048 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| admin1_code | varchar | 8000 | 1 |  |  |  |
| admin1_name | varchar | 8000 | 1 |  |  |  |
| admin2_code | varchar | 8000 | 1 |  |  |  |
| admin2_name | varchar | 8000 | 1 |  |  |  |
| locality | varchar | 8000 | 1 |  |  |  |
| sublocality | varchar | 8000 | 1 |  |  |  |
| metro_area_code | varchar | 8000 | 1 |  |  |  |
| metro_area_name | varchar | 8000 | 1 |  |  |  |
| iso2 | varchar | 8000 | 1 |  |  |  |
| iso3 | varchar | 8000 | 1 |  |  |  |
| m49_code | varchar | 8000 | 1 |  |  |  |
| currency_code | varchar | 8000 | 1 |  |  |  |
| tzid | varchar | 8000 | 1 |  |  |  |
| latitude | float | 8 | 1 |  |  |  |
| longitude | float | 8 | 1 |  |  |  |
| geohash | varchar | 8000 | 1 |  |  |  |
| h3_res7 | varchar | 8000 | 1 |  |  |  |
| valid_from | date | 3 | 1 |  |  |  |
| valid_to | date | 3 | 1 |  |  |  |
| is_current | bit | 1 | 1 |  |  |  |
| source_system | varchar | 8000 | 1 |  |  |  |
| confidence | decimal | 5 | 1 |  |  |  |
| last_updated_utc | datetime2 | 8 | 1 |  |  |  |
