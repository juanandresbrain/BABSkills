# dbo.work_rec_verification

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| rec_id | tran_id_datatype | 9 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| rec_store_no | int | 4 | 1 |  |  |  |
| rec_register_no | smallint | 2 | 1 |  |  |  |
| reconciliation_date | smalldatetime | 4 | 1 |  |  |  |
| audit_activity_flag | smallint | 2 | 0 |  |  |  |
| new_audit_activity_flag | smallint | 2 | 0 |  |  |  |
| old_activity_descr | nvarchar | 510 | 1 |  |  |  |
| new_activity_descr | nvarchar | 510 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
