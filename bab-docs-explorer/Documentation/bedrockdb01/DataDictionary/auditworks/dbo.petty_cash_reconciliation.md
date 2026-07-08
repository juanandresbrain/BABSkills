# dbo.petty_cash_reconciliation

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| entry_datetime | datetime | 8 | 0 |  |  |  |
| petty_cash_amount | money | 8 | 0 |  |  |  |
| discrepancy_amount | money | 8 | 0 |  |  |  |
