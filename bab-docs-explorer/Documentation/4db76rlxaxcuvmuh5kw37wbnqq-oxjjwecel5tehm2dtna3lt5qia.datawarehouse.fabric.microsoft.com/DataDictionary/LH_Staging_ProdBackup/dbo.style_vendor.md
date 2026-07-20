# dbo.style_vendor

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_vendor_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| vendor_style | varchar | 8000 | 1 |  |  |  |
| primary_vendor_flag | bit | 1 | 1 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
