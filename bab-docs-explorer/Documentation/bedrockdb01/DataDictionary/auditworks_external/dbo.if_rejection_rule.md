# dbo.if_rejection_rule

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_rejection_reason | smallint | 2 | 0 |  |  |  |
| allow_deferral | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| if_rejection_description | nvarchar | 510 | 1 |  |  |  |
| active_rejection_rule | tinyint | 1 | 1 |  |  |  |
| transaction_line_flag | tinyint | 1 | 1 |  |  |  |
| external_detection | tinyint | 1 | 0 |  |  |  |
| allow_override | tinyint | 1 | 0 |  |  |  |
| user_id | int | 4 | 1 |  |  |  |
| SQL_TXT | nvarchar | -1 | 1 |  |  |  |
| SQL_QRY | nvarchar | -1 | 1 |  |  |  |
| SQL_QRY_OBJ | text | 16 | 1 |  |  |  |
| revalidation_ENTY_TYPE | nvarchar | 100 | 1 |  |  |  |
