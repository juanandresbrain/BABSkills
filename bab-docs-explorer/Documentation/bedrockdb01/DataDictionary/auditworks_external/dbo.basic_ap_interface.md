# dbo.basic_ap_interface

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| company_no | tinyint | 1 | 0 |  |  |  |
| bank_code | smallint | 2 | 0 |  |  |  |
| filler_1 | char | 2 | 0 |  |  |  |
| invoice_no | numeric | 9 | 0 |  |  |  |
| invoice_type | char | 1 | 0 |  |  |  |
| hold_flag | char | 1 | 0 |  |  |  |
| invoice_remark | char | 32 | 0 |  |  |  |
| gross_invoice_amount | int | 4 | 0 |  |  |  |
| discount_amount | int | 4 | 0 |  |  |  |
| entered_date | char | 6 | 0 |  |  |  |
| invoice_date | char | 6 | 0 |  |  |  |
| due_date | char | 6 | 0 |  |  |  |
| discount_date | char | 6 | 0 |  |  |  |
| first_expense_account | char | 14 | 0 |  |  |  |
| gl_expense_accounts | char | 126 | 0 |  |  |  |
| first_distribution_amount | int | 4 | 0 |  |  |  |
| gl_distribution_amount1 | int | 4 | 0 |  |  |  |
| gl_distribution_amount2 | int | 4 | 0 |  |  |  |
| gl_distribution_amount3 | int | 4 | 0 |  |  |  |
| gl_distribution_amount4 | int | 4 | 0 |  |  |  |
| gl_distribution_amount5 | int | 4 | 0 |  |  |  |
| gl_distribution_amount6 | int | 4 | 0 |  |  |  |
| gl_distribution_amount7 | int | 4 | 0 |  |  |  |
| gl_distribution_amount8 | int | 4 | 0 |  |  |  |
| gl_distribution_amount9 | int | 4 | 0 |  |  |  |
| vendor_name | char | 30 | 0 |  |  |  |
| address_1 | char | 30 | 0 |  |  |  |
| address_2 | char | 30 | 0 |  |  |  |
| telephone_no | char | 16 | 0 |  |  |  |
| filler_2 | char | 10 | 0 |  |  |  |
