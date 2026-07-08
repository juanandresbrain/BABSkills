# dbo.settlement_service

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| service_name | nvarchar | 60 | 0 |  |  |  |
| chain_name | nvarchar | 60 | 1 |  |  |  |
| chain_merchant_id | nvarchar | 60 | 1 |  |  |  |
| service_parameters | nvarchar | 120 | 1 |  |  |  |
| merchandise_description | nvarchar | 60 | 1 |  |  |  |
| store_merchant_id_length | tinyint | 1 | 1 |  |  |  |
| store_merchant_id_alpha | tinyint | 1 | 1 |  |  |  |
| last_posting_date | datetime | 8 | 1 |  |  |  |
| prev_file_sequence_no | nvarchar | 12 | 1 |  |  |  |
| prev_creation_successful | tinyint | 1 | 1 |  |  |  |
| auth_format_default | tinyint | 1 | 0 |  |  |  |
| store_live_date_default | smalldatetime | 4 | 1 |  |  |  |
| store_param1_descr_code | smallint | 2 | 1 |  |  |  |
| store_param2_descr_code | smallint | 2 | 1 |  |  |  |
