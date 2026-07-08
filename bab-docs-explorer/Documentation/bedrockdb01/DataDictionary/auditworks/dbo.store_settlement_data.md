# dbo.store_settlement_data

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| deposit_source_id | smallint | 2 | 0 |  |  |  |
| store_merchant_id | nvarchar | 60 | 0 |  |  |  |
| auth_format | tinyint | 1 | 0 |  |  |  |
| store_live_flag | tinyint | 1 | 1 |  |  |  |
| store_live_date | smalldatetime | 4 | 1 |  |  |  |
| store_parameter1 | nvarchar | 100 | 1 |  |  |  |
| store_parameter2 | nvarchar | 100 | 1 |  |  |  |
