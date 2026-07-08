# dbo.export_transl_pcreg

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| version_no | tinyint | 1 | 0 |  |  |  |
| rec_type | char | 2 | 0 |  |  |  |
| descriptor | char | 4 | 0 |  |  |  |
| transaction_type | char | 3 | 0 |  |  |  |
| transaction_subtype | char | 1 | 0 |  |  |  |
| data_poll_pos | char | 3 | 0 |  |  |  |
| data_poll_length | char | 3 | 0 |  |  |  |
| data_type | char | 1 | 0 |  |  |  |
| data_from | char | 22 | 0 |  |  |  |
| data_to | char | 22 | 0 |  |  |  |
| data_replace_with_constant | char | 22 | 0 |  |  |  |
| data_decimals_assume | char | 3 | 0 |  |  |  |
| data_repeat | char | 1 | 0 |  |  |  |
| transaction_delimitor | char | 1 | 0 |  |  |  |
| data_precedes_amount | char | 1 | 0 |  |  |  |
| prorate | char | 1 | 0 |  |  |  |
| discount_table | char | 1 | 0 |  |  |  |
| discount_column | char | 3 | 0 |  |  |  |
| discountable | char | 2 | 0 |  |  |  |
| output_file | char | 1 | 0 |  |  |  |
| output_column | char | 3 | 0 |  |  |  |
| seq | tinyint | 1 | 0 |  |  |  |
| tax_transaction_type | char | 4 | 0 |  |  |  |
