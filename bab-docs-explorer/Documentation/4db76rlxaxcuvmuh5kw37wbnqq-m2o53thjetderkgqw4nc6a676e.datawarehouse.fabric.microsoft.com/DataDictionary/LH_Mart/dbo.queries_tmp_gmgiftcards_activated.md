# dbo.queries_tmp_gmgiftcards_activated

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| gross_line_amount | decimal | 9 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| db_cr_none | int | 4 | 1 |  |  |  |
| DFLT_CRNCY_CODE | varchar | 8000 | 1 |  |  |  |
