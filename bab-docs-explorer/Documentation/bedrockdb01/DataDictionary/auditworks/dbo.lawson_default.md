# dbo.lawson_default

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| run_group | char | 12 | 1 |  |  |  |
| seq_number | char | 6 | 1 |  |  |  |
| company | char | 4 | 1 |  |  |  |
| old_company | char | 35 | 1 |  |  |  |
| old_acct_no | char | 160 | 1 |  |  |  |
| source_code | char | 2 | 1 |  |  |  |
| calendar_date | char | 8 | 1 |  |  |  |
| refer | char | 10 | 1 |  |  |  |
| description | char | 30 | 1 |  |  |  |
| currency | char | 5 | 1 |  |  |  |
| units_amt | char | 15 | 1 |  |  |  |
| units_amt_s | char | 1 | 1 |  |  |  |
| trans_amt | char | 15 | 1 |  |  |  |
| trans_amt_s | char | 1 | 1 |  |  |  |
| base_amt | char | 15 | 1 |  |  |  |
| base_amt_s | char | 1 | 1 |  |  |  |
| baserate | char | 12 | 1 |  |  |  |
| baserate_s | char | 1 | 1 |  |  |  |
| system | char | 2 | 1 |  |  |  |
| program_code | char | 5 | 1 |  |  |  |
| autorev | char | 1 | 1 |  |  |  |
| posting_date | char | 8 | 1 |  |  |  |
| activity | char | 15 | 1 |  |  |  |
| acct_catg | char | 5 | 1 |  |  |  |
| doc_nbr | char | 15 | 1 |  |  |  |
| to_base_amt | char | 15 | 1 |  |  |  |
| to_base_amt_s | char | 1 | 1 |  |  |  |
| effect_date | char | 8 | 1 |  |  |  |
| jnl_book_nbr | char | 12 | 1 |  |  |  |
| mx1 | char | 20 | 1 |  |  |  |
| mx2 | char | 20 | 1 |  |  |  |
| mx3 | char | 20 | 1 |  |  |  |
| subledger_grouping | tinyint | 1 | 0 |  |  |  |
| refer_source | tinyint | 1 | 0 |  |  |  |
| run_group_source | tinyint | 1 | 0 |  |  |  |
| preceed_amt_with_sign | tinyint | 1 | 1 |  |  |  |
| calendar_date_fmt | tinyint | 1 | 1 |  |  |  |
