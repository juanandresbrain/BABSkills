# dbo.TransactionTaxFactsDynamicsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| line_sequence | numeric | 5 | 1 |  |  |  |
| line_object_type | tinyint | 1 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| gross_line_amount | numeric | 9 | 1 |  |  |  |
| pos_discount_amount | numeric | 9 | 1 |  |  |  |
| taxable_amount | numeric | 9 | 1 |  |  |  |
| nontaxable_amount | numeric | 9 | 1 |  |  |  |
| combined_rate | numeric | 5 | 1 |  |  |  |
| tax_amount_expected | numeric | 9 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
