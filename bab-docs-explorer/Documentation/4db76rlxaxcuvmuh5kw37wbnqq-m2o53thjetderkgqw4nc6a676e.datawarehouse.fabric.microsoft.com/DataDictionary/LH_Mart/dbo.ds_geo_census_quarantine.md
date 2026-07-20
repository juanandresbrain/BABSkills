# dbo.ds_geo_census_quarantine

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| country_code | varchar | 8000 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| zcta5 | varchar | 8000 | 1 |  |  |  |
| zcta_name | varchar | 8000 | 1 |  |  |  |
| acs_year | int | 4 | 1 |  |  |  |
| api_source_url | varchar | 8000 | 1 |  |  |  |
| load_utc | datetime2 | 8 | 1 |  |  |  |
