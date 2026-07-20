# dbo.ma_01_upc

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| upc_type | int | 4 | 1 |  |  |  |
| upc_number | varchar | 8000 | 1 |  |  |  |
| activation_date | datetime2 | 8 | 1 |  |  |  |
| last_activity_date | datetime2 | 8 | 1 |  |  |  |
