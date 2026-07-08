# dbo.cust_liability_xref

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_type | tinyint | 1 | 0 |  |  |  |
| old_reference_no | nvarchar | 40 | 0 |  |  |  |
| old_key_store_no | int | 4 | 0 |  |  |  |
| new_reference_no | nvarchar | 40 | 0 |  |  |  |
| new_key_store_no | int | 4 | 0 |  |  |  |
| renumber_datetime | datetime | 8 | 0 |  |  |  |
