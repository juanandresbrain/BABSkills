# dbo.price_change_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_location_id | decimal | 9 | 0 | YES |  |  |
| price_change_id | decimal | 9 | 0 |  |  |  |
| printed_status | bit | 1 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| pricing_group_id | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.add_promtional_event_$sp](../../StoredProcedures/me_01/dbo.add_promtional_event_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.pc_calc_total_affected_units_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_affected_units_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)
- [me_01: dbo.pcm_pre_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_pre_issue_pc_$sp.md)
- [me_01: dbo.plu_pc_queue_$sp](../../StoredProcedures/me_01/dbo.plu_pc_queue_$sp.md)

