# dbo.distribution_c

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 |  |  |  |
| algorithm_key | nvarchar | 80 | 0 |  |  |  |
| sales_plan_weight_pct | smallint | 2 | 0 |  |  |  |
| sales_weight_pct | smallint | 2 | 0 |  |  |  |
| sales_from_calendar_week_id | decimal | 9 | 1 |  |  |  |
| sales_to_calendar_week_id | decimal | 9 | 1 |  |  |  |
| sales_data_basis | smallint | 2 | 1 |  |  |  |
| plans_from_calendar_week_id | decimal | 9 | 1 |  |  |  |
| plans_to_calendar_week_id | decimal | 9 | 1 |  |  |  |
| plan_hierarchy_group_id | int | 4 | 1 |  |  |  |
| weeks_of_supply_loc_need | smallint | 2 | 1 |  |  |  |
| incl_effect_inv_loc_need_flag | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

