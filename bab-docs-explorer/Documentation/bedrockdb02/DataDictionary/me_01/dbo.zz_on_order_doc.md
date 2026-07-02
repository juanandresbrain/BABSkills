# dbo.zz_on_order_doc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_audit_trail_id | decimal | 9 | 0 |  |  |  |
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| application | nvarchar | 20 | 0 |  |  |  |
| activity | nvarchar | 40 | 1 |  |  |  |
| application_type_id | nvarchar | 30 | 1 |  |  |  |
| application_type | nvarchar | 80 | 0 |  |  |  |
| application_identifier | nvarchar | 40 | 1 |  |  |  |
| application_level | nvarchar | 80 | 1 |  |  |  |
| application_key | nvarchar | 510 | 1 |  |  |  |
| action | nvarchar | 40 | 1 |  |  |  |
| field_affected | nvarchar | 80 | 1 |  |  |  |
| old_value | nvarchar | 510 | 1 |  |  |  |
| new_value | nvarchar | 510 | 1 |  |  |  |
| status | nvarchar | 40 | 1 |  |  |  |
| employee_last_name | nvarchar | 60 | 0 |  |  |  |
| employee_first_name | nvarchar | 60 | 0 |  |  |  |

