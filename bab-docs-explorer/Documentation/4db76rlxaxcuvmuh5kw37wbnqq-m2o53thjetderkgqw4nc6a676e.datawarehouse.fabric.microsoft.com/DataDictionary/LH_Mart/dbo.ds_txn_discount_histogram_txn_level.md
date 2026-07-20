# dbo.ds_txn_discount_histogram_txn_level

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| gross_amount | decimal | 9 | 1 |  |  |  |
| net_amount | decimal | 9 | 1 |  |  |  |
| disc_amount | decimal | 9 | 1 |  |  |  |
| disc_amount_bucket_$1 | varchar | 8000 | 1 |  |  |  |
| disc_amount_bucket_$1_index | int | 4 | 1 |  |  |  |
| gross_amount_bucket_$1 | varchar | 8000 | 1 |  |  |  |
| gross_amount_bucket_$1_index | int | 4 | 1 |  |  |  |
| net_amount_bucket_$1 | varchar | 8000 | 1 |  |  |  |
| net_amount_bucket_$1_index | int | 4 | 1 |  |  |  |
| disc_amount_bucket_$5 | varchar | 8000 | 1 |  |  |  |
| disc_amount_bucket_$5_index | int | 4 | 1 |  |  |  |
| gross_amount_bucket_$5 | varchar | 8000 | 1 |  |  |  |
| gross_amount_bucket_$5_index | int | 4 | 1 |  |  |  |
| net_amount_bucket_$5 | varchar | 8000 | 1 |  |  |  |
| net_amount_bucket_$5_index | int | 4 | 1 |  |  |  |
| disc_amount_bucket_$10 | varchar | 8000 | 1 |  |  |  |
| disc_amount_bucket_$10_index | int | 4 | 1 |  |  |  |
| gross_amount_bucket_$10 | varchar | 8000 | 1 |  |  |  |
| gross_amount_bucket_$10_index | int | 4 | 1 |  |  |  |
| net_amount_bucket_$10 | varchar | 8000 | 1 |  |  |  |
| net_amount_bucket_$10_index | int | 4 | 1 |  |  |  |
