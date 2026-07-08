# dbo.Ld_POS_Audits_OneTime_dlr_save

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| modified_date | datetime | 8 | 1 |  |  |  |
| dm_deleted_y_n | char | 1 | 1 |  |  |  |
| dm_deleted_date | datetime | 8 | 1 |  |  |  |
| seqno | int | 4 | 0 | YES |  |  |
