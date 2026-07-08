# dbo.copy_dayend_summarized_data

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| rebuild_type | nvarchar | 2 | 1 |  |  |  |
| posting_datetime | datetime | 8 | 1 |  |  |  |
