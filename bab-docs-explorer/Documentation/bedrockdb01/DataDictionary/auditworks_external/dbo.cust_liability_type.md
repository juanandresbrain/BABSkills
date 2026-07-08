# dbo.cust_liability_type

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_type | tinyint | 1 | 0 |  |  |  |
| tracking_id | smallint | 2 | 0 |  |  |  |
| tracking_id_description | nvarchar | 510 | 1 |  |  |  |
| expiry_days | smallint | 2 | 1 |  |  |  |
| customer_liability_group | smallint | 2 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| active_flag | tinyint | 1 | 1 |  |  |  |
| copy_from_reference_type | tinyint | 1 | 1 |  |  |  |
