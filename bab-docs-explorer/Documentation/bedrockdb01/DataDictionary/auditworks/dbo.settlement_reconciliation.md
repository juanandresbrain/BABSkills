# dbo.settlement_reconciliation

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deposit_destination | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| deposit_category | smallint | 2 | 0 |  |  |  |
| deposit_source | smallint | 2 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transmission_date | smalldatetime | 4 | 0 |  |  |  |
| transmission_id | numeric | 9 | 0 |  |  |  |
| deposit_date | smalldatetime | 4 | 0 |  |  |  |
| transmission_amount | money | 8 | 0 |  |  |  |
| fees | money | 8 | 0 |  |  |  |
| actual_net_deposit | money | 8 | 0 |  |  |  |
