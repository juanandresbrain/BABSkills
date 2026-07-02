# dbo.inventory_control

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_id | decimal | 9 | 0 | YES |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| count_date | smalldatetime | 4 | 0 |  |  |  |
| valuation_date | smalldatetime | 4 | 0 |  |  |  |
| update_type | smallint | 2 | 0 |  |  |  |
| use_level_flag | bit | 1 | 0 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.freeze_inventory_$sp](../../StoredProcedures/me_01/dbo.freeze_inventory_$sp.md)
- [me_01: dbo.pi_process_loc_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_$sp.md)
- [me_01: dbo.pi_process_loc_ols_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_ols_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.update_phys_inv_table_$sp](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp.md)
- [me_01: dbo.update_phys_inv_table_$sp_091609](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp_091609.md)

