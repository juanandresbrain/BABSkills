# dbo.MSqreader_history

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| agent_id | int | 4 | 0 |  |  |  |
| publication_id | int | 4 | 1 |  |  |  |
| runstatus | int | 4 | 0 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| time | datetime | 8 | 0 |  |  |  |
| duration | int | 4 | 0 |  |  |  |
| comments | nvarchar | 2000 | 0 |  |  |  |
| transaction_id | nvarchar | 80 | 1 |  |  |  |
| transaction_status | int | 4 | 1 |  |  |  |
| transactions_processed | int | 4 | 1 |  |  |  |
| commands_processed | int | 4 | 1 |  |  |  |
| delivery_rate | float | 8 | 0 |  |  |  |
| transaction_rate | float | 8 | 0 |  |  |  |
| subscriber | sysname | 256 | 1 |  |  |  |
| subscriberdb | sysname | 256 | 1 |  |  |  |
| error_id | int | 4 | 1 |  |  |  |
| timestamp | timestamp | 8 | 0 |  |  |  |
