# dbo.metric_facts_archive

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| metric_facts_key | bigint | 8 | 1 |  |  |  |
| metric_dim_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| amount | decimal | 9 | 1 |  |  |  |
| ly_date_key | int | 4 | 1 |  |  |  |
| ly_amount | decimal | 9 | 1 |  |  |  |
