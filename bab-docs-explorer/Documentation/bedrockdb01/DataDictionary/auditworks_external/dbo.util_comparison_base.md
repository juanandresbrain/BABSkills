# dbo.util_comparison_base

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comparison_id | int | 4 | 0 |  |  |  |
| test_case_description | nvarchar | 510 | 0 |  |  |  |
| comparison_type | smallint | 2 | 0 |  |  |  |
| from_store_no | int | 4 | 1 |  |  |  |
| to_store_no | int | 4 | 1 |  |  |  |
| from_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| to_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| interface_id | tinyint | 1 | 1 |  |  |  |
| comments | text | 16 | 1 |  |  |  |
| status_message | nvarchar | 510 | 1 |  |  |  |
| extra_count | int | 4 | 1 |  |  |  |
| missing_count | int | 4 | 1 |  |  |  |
| different_count | int | 4 | 1 |  |  |  |
| minor_difference_count | int | 4 | 1 |  |  |  |
| last_comparison_datetime | datetime | 8 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
