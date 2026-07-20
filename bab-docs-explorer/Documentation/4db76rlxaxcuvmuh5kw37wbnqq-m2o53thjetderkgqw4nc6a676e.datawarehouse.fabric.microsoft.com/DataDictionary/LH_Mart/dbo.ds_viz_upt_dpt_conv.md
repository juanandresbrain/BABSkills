# dbo.ds_viz_upt_dpt_conv

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| actual_date | datetime2 | 8 | 1 |  |  |  |
| storekey | int | 4 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| num_txn | bigint | 8 | 1 |  |  |  |
| conversion | float | 8 | 1 |  |  |  |
| average_gross_amount | decimal | 13 | 1 |  |  |  |
| average_units | float | 8 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| transaction_unit_price | decimal | 5 | 1 |  |  |  |
