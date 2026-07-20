# dbo.conversion_rate_dim

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| conversion_rate_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| ca_to_us | float | 8 | 1 |  |  |  |
| us_to_ca | float | 8 | 1 |  |  |  |
