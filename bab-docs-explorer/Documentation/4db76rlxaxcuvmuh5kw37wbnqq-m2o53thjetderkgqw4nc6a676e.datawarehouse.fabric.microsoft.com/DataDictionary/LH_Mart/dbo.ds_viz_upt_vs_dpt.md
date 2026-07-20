# dbo.ds_viz_upt_vs_dpt

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| current_price | decimal | 9 | 1 |  |  |  |
| original_price | decimal | 9 | 1 |  |  |  |
| price_type | varchar | 8000 | 1 |  |  |  |
| num_txns | bigint | 8 | 1 |  |  |  |
| sum_gross_amount | decimal | 17 | 1 |  |  |  |
| sum_net_amount | decimal | 17 | 1 |  |  |  |
| UPT | float | 8 | 1 |  |  |  |
| DPT | decimal | 17 | 1 |  |  |  |
