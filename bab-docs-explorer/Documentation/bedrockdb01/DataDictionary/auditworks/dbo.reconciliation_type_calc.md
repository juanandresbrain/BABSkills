# dbo.reconciliation_type_calc

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_type | smallint | 2 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| rec_amount_type | tinyint | 1 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 0 |  |  |  |
| contribution_sign | smallint | 2 | 0 |  |  |  |
| active_rec_type_required | smallint | 2 | 1 |  |  |  |
