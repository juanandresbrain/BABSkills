# dbo.vendor_parameter_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_parameter_set_id | int | 4 | 0 | YES |  |  |
| imat_flow_id | int | 4 | 0 |  |  |  |
| vendor_parameter_set_code | nvarchar | 40 | 0 |  |  |  |
| vendor_parameter_set_desc | nvarchar | 60 | 0 |  |  |  |
| tolerance_amount | decimal | 9 | 0 |  |  |  |
| tolerance_percent | decimal | 5 | 0 |  |  |  |
| edi_input_terms_override | smallint | 2 | 0 |  |  |  |
| manual_input_terms_override | smallint | 2 | 0 |  |  |  |
| sys_gen_input_terms_override | bit | 1 | 0 |  |  |  |
| exchange_difference_accounting | smallint | 2 | 0 |  |  |  |
| release_accepted_matches_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| import_proc_or_reproc_delay | tinyint | 1 | 0 |  |  |  |
| manual_proc_or_reproc_delay | tinyint | 1 | 0 |  |  |  |
| import_proc_delay_days | tinyint | 1 | 0 |  |  |  |
| import_reproc_delay_days | tinyint | 1 | 0 |  |  |  |
| manual_proc_delay_days | tinyint | 1 | 0 |  |  |  |
| manual_reproc_delay_days | tinyint | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| currency_id | decimal | 9 | 0 |  |  |  |
| tax_tolerance_amount | decimal | 9 | 0 |  |  |  |

