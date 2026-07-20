# dbo.transactionfactsdynamics_testtc1

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| GAAP_sales_amount | decimal | 17 | 1 |  |  |  |
| upsell_discount_amount | decimal | 9 | 1 |  |  |  |
| total_discount_amount | decimal | 17 | 1 |  |  |  |
| GAAP_transaction_flag | int | 4 | 1 |  |  |  |
| coupon_discount_amount | decimal | 17 | 1 |  |  |  |
