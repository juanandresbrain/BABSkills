# dbo.media_parameter_selection

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| effective_until_date | datetime | 8 | 1 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| conversion_outstanding | tinyint | 1 | 0 |  |  |  |
