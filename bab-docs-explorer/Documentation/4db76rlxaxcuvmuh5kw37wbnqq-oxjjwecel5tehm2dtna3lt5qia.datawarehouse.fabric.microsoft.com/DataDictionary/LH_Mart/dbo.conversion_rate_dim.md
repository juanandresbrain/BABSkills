# dbo.conversion_rate_dim

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| conversion_rate_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| ca_to_us | float | 8 | 1 |  |  |  |
| us_to_ca | float | 8 | 1 |  |  |  |
