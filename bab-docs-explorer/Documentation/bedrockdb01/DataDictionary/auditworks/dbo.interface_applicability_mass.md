# dbo.interface_applicability_mass

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| update_timing | smallint | 2 | 0 |  |  |  |
| interface_voided_transactions | tinyint | 1 | 0 |  |  |  |
| live_date | smalldatetime | 4 | 1 |  |  |  |
