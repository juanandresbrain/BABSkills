# dbo.cust_liability_summary

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| tracking_id | smallint | 2 | 0 |  |  |  |
| liability_incurred_date | smalldatetime | 4 | 0 |  |  |  |
| change_in_liability_balance | money | 8 | 0 |  |  |  |
| change_in_receivable_balance | money | 8 | 0 |  |  |  |
| change_in_stocked_amount | money | 8 | 0 |  |  |  |
| change_in_stocked_qty | int | 4 | 0 |  |  |  |
