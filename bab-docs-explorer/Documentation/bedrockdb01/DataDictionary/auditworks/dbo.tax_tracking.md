# dbo.tax_tracking

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_level | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| tax_category | tinyint | 1 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| combined_rate | numeric | 5 | 0 |  |  |  |
| tax_on_tax_level | tinyint | 1 | 0 |  |  |  |
| tax_on_combined_rate | numeric | 5 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| taxable_merchandise_amount | money | 8 | 0 |  |  |  |
| taxable_fee_amount | money | 8 | 0 |  |  |  |
| taxable_expense_amount | money | 8 | 1 |  |  |  |
| nontaxable_merchandise_amount | money | 8 | 0 |  |  |  |
| nontaxable_fee_amount | money | 8 | 0 |  |  |  |
| tax_amount_collected | money | 8 | 0 |  |  |  |
| tax_amount_expected | money | 8 | 0 |  |  |  |
| tax_amount_paid | money | 8 | 1 |  |  |  |
| rollup_flag | tinyint | 1 | 0 |  |  |  |
| posting_date | datetime | 8 | 1 |  |  |  |
