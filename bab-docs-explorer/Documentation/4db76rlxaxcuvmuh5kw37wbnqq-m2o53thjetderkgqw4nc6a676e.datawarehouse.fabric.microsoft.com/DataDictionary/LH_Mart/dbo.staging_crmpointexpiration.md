# dbo.staging_crmpointexpiration

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_id | int | 4 | 1 |  |  |  |
| last_date_points_expired | datetime2 | 8 | 1 |  |  |  |
| last_no_points_expired | decimal | 9 | 1 |  |  |  |
| country_code | varchar | 8000 | 1 |  |  |  |
