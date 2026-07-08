# dbo.tblComparePartyDepositsSJ

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SJ_OrderNumber | varchar | 50 | 1 |  |  |  |
| SJ_entry_date_time | datetime | 8 | 0 |  |  |  |
| SJ_total_deposit | money | 8 | 1 |  |  |  |
| SJ_iExported | tinyint | 1 | 0 |  |  |  |
| SJ_store_no | int | 4 | 1 |  |  |  |
| SJ_register_no | tinyint | 1 | 1 |  |  |  |
| SJ_transaction_no | varchar | 10 | 1 |  |  |  |
| sourceTable | varchar | 100 | 1 |  |  |  |
