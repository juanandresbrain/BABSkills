# dbo.util_comparison_key

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | int | 4 | 0 |  |  |  |
| transaction_key | numeric | 9 | 0 |  |  |  |
| sequence_datetime | datetime | 8 | 1 |  |  |  |
| comparison_key | nvarchar | 510 | 1 |  |  |  |
| ref_type | tinyint | 1 | 1 |  |  |  |
