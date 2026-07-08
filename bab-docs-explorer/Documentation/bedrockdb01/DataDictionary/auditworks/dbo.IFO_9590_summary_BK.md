# dbo.IFO_9590_summary_BK

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | numeric | 9 | 1 |  |  |  |
| execution_date | datetime | 8 | 1 |  |  |  |
| store | int | 4 | 1 |  |  |  |
| register | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| transaction_no | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| amount | money | 8 | 1 |  |  |  |
| card_type | char | 1 | 1 |  |  |  |
| account_no | varchar | 20 | 1 |  |  |  |
| auth_no | varchar | 20 | 1 |  |  |  |
| data1 | numeric | 9 | 1 |  |  |  |
| data2 | numeric | 9 | 1 |  |  |  |
| data3 | varchar | 255 | 1 |  |  |  |
