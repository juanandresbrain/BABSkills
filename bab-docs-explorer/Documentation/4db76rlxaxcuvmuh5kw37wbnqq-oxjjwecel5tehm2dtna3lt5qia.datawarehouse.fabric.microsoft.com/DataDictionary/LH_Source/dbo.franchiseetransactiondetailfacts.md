# dbo.franchiseetransactiondetailfacts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| transaction_id | varchar | 8000 | 1 |  |  |  |
| transaction_line_seq | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 13 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| units | bigint | 8 | 1 |  |  |  |
| unit_disc_amount | decimal | 13 | 1 |  |  |  |
| transaction_no | varchar | 8000 | 1 |  |  |  |
| vat_tax_amount | decimal | 13 | 1 |  |  |  |
| upsell_disc_allocated | int | 4 | 1 |  |  |  |
| ext_cost | decimal | 13 | 1 |  |  |  |
