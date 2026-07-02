# dbo.parameter_imat

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_imat_id | tinyint | 1 | 0 | YES |  |  |
| cutoff_day | tinyint | 1 | 0 |  |  |  |
| invoice_history_days | smallint | 2 | 0 |  |  |  |
| receipt_history_days | smallint | 2 | 0 |  |  |  |
| invoice_batch_no_rec_flag | bit | 1 | 0 |  |  |  |
| invoice_no_rec_flag | bit | 1 | 0 |  |  |  |
| max_invoice_length | tinyint | 1 | 0 |  |  |  |
| invoice_number_mask | nvarchar | 40 | 0 |  |  |  |
| first_invoice_number | nvarchar | 40 | 0 |  |  |  |
| last_invoice_number | nvarchar | 40 | 0 |  |  |  |
| last_gen_invoice_number | nvarchar | 40 | 1 |  |  |  |
| gl_account_id_for_insurance | decimal | 9 | 0 |  |  |  |
| gl_account_id_for_freightin | decimal | 9 | 0 |  |  |  |
| gl_account_id_for_freightout | decimal | 9 | 0 |  |  |  |
| gl_account_id_for_misc | decimal | 9 | 0 |  |  |  |
| gl_account_id_for_purge_debit | decimal | 9 | 1 |  |  |  |
| gl_account_id_for_purge_credit | decimal | 9 | 1 |  |  |  |
| process_number_mask | nvarchar | 40 | 0 |  |  |  |
| first_process_number | nvarchar | 40 | 0 |  |  |  |
| last_process_number | nvarchar | 40 | 0 |  |  |  |
| last_gen_process_number | nvarchar | 40 | 1 |  |  |  |
| process_no_rec_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| match_on_taxes_flag | bit | 1 | 0 |  |  |  |
| include_tax_in_subject_to_terms_discount | bit | 1 | 0 |  |  |  |
| export_gl_company_flag | bit | 1 | 0 |  |  |  |

