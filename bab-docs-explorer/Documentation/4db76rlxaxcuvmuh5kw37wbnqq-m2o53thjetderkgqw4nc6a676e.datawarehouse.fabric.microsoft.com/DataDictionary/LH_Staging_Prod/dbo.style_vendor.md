# dbo.style_vendor

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
