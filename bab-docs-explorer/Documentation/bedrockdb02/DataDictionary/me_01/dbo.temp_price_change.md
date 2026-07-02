# dbo.temp_price_change

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 1 |  |  |  |
| imp_price_change_id | decimal | 9 | 1 |  |  |  |
| temp_price_change_id | decimal | 9 | 0 |  |  |  |
| category_id | decimal | 9 | 1 |  |  |  |
| pricing_rule_id | decimal | 9 | 0 |  |  |  |
| price_change_no | nvarchar | 40 | 0 |  |  |  |
| price_change_status | smallint | 2 | 0 |  |  |  |
| price_change_description | nvarchar | 120 | 1 |  |  |  |
| price_change_duration | smallint | 2 | 1 |  |  |  |
| price_change_document_type | smallint | 2 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_to_date | smalldatetime | 4 | 1 |  |  |  |
| terminate_on_date | smalldatetime | 4 | 1 |  |  |  |
| issue_date | smalldatetime | 4 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| price_status_override | bit | 1 | 1 |  |  |  |
| location_grouping | smallint | 2 | 0 |  |  |  |
| calculation_method | smallint | 2 | 1 |  |  |  |
| calculation_value | decimal | 9 | 1 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| override_price_exceptions | bit | 1 | 1 |  |  |  |
| disable_print_by_location_flag | bit | 1 | 0 |  |  |  |
| approval_status | smallint | 2 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| status_date | smalldatetime | 4 | 0 |  |  |  |
| last_copy_date | smalldatetime | 4 | 0 |  |  |  |
| calculation_date | smalldatetime | 4 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| total_cost | decimal | 9 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| state_no | smallint | 2 | 0 |  |  |  |
| total_units | int | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| generate_tickets | smallint | 2 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| total_valuation_cost | decimal | 9 | 1 |  |  |  |
| promotional_event_flag | bit | 1 | 0 |  |  |  |
| submitted_by_id | decimal | 9 | 1 |  |  |  |
| total_affected_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_$sp.md)
- [me_01: dbo.import_pc_adjust_temp_pc_id_$sp](../../StoredProcedures/me_01/dbo.import_pc_adjust_temp_pc_id_$sp.md)
- [me_01: dbo.import_pc_batch_issue_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_issue_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)

