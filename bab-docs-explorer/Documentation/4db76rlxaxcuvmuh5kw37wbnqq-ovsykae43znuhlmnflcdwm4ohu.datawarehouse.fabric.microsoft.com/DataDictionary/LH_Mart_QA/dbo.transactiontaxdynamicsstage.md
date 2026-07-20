# dbo.transactiontaxdynamicsstage

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| line_sequence | decimal | 5 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_action | int | 4 | 1 |  |  |  |
| gross_line_amount | decimal | 9 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| taxable_amount | decimal | 9 | 1 |  |  |  |
| nontaxable_amount | decimal | 9 | 1 |  |  |  |
| combined_rate | decimal | 5 | 1 |  |  |  |
| tax_amount_expected | decimal | 9 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| tax_level | int | 4 | 1 |  |  |  |
| line_id | int | 4 | 1 |  |  |  |
