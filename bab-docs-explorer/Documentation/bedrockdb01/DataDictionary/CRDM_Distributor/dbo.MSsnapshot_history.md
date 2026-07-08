# dbo.MSsnapshot_history

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| agent_id | int | 4 | 0 |  |  |  |
| runstatus | int | 4 | 0 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| time | datetime | 8 | 0 |  |  |  |
| duration | int | 4 | 0 |  |  |  |
| comments | nvarchar | 2000 | 0 |  |  |  |
| delivered_transactions | int | 4 | 0 |  |  |  |
| delivered_commands | int | 4 | 0 |  |  |  |
| delivery_rate | float | 8 | 0 |  |  |  |
| error_id | int | 4 | 0 |  |  |  |
| timestamp | timestamp | 8 | 0 |  |  |  |
