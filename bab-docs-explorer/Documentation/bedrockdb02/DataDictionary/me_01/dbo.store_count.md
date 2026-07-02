# dbo.store_count

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_count_id | decimal | 9 | 0 | YES |  |  |
| document_no | nchar | 12 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| completion_date | datetime | 8 | 1 |  |  |  |
| completed_by_employee_id | decimal | 9 | 1 |  |  |  |
| inventory_control_id | decimal | 9 | 0 |  |  |  |
| update_inventory_action | tinyint | 1 | 0 |  |  |  |
| count_date | datetime | 8 | 1 |  |  |  |
| description | nvarchar | 120 | 1 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_activity_date | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pi_move_store_count_$sp](../../StoredProcedures/me_01/dbo.pi_move_store_count_$sp.md)

