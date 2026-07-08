# dbo.z_tran_counts

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| sa_reject_count | smallint | 2 | 0 |  |  |  |
| if_reject_count | smallint | 2 | 0 |  |  |  |
| valid_count | smallint | 2 | 0 |  |  |  |
