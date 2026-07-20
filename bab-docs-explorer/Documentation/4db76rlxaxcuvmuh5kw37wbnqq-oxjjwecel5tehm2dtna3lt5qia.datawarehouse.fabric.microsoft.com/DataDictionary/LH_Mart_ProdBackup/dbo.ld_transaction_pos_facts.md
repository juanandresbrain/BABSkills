# dbo.ld_transaction_pos_facts

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| Transaction_No | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 1 |  |  |  |
| party_y_n | varchar | 8000 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| upsell_disc_allocated | decimal | 9 | 1 |  |  |  |
