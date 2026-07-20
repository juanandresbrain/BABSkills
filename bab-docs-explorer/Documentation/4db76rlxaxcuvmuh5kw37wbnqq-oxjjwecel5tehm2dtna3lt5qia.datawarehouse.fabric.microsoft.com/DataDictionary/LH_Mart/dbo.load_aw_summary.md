# dbo.load_aw_summary

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| aw_units | decimal | 9 | 1 |  |  |  |
| dm_units | decimal | 9 | 1 |  |  |  |
| aw_sales | decimal | 9 | 1 |  |  |  |
| dm_sales | decimal | 9 | 1 |  |  |  |
| unit_diff | decimal | 9 | 1 |  |  |  |
| unit_pct_diff | decimal | 9 | 1 |  |  |  |
| sales_diff | decimal | 9 | 1 |  |  |  |
| sales_pct_diff | decimal | 9 | 1 |  |  |  |
