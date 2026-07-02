# dbo.core_replication_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| core_replication_queue_id | decimal | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | nvarchar | 4 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_id | decimal | 9 | 1 |  |  |  |
| primary_entity_key | nvarchar | 40 | 1 |  |  |  |
| secondary_entity_key | nvarchar | 40 | 1 |  |  |  |
| replication_data | nvarchar | 210 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_like_location_prices_$sp](../../StoredProcedures/me_01/dbo.copy_like_location_prices_$sp.md)
- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)
- [me_01: dbo.plu_deleted_dept_queue_$sp](../../StoredProcedures/me_01/dbo.plu_deleted_dept_queue_$sp.md)
- [me_01: dbo.plu_deleted_item_queue_$sp](../../StoredProcedures/me_01/dbo.plu_deleted_item_queue_$sp.md)
- [me_01: dbo.plu_deleted_style_queue_$sp](../../StoredProcedures/me_01/dbo.plu_deleted_style_queue_$sp.md)
- [me_01: dbo.plu_dept_queue_$sp](../../StoredProcedures/me_01/dbo.plu_dept_queue_$sp.md)
- [me_01: dbo.plu_hg_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_queue_$sp.md)
- [me_01: dbo.plu_item_queue_$sp](../../StoredProcedures/me_01/dbo.plu_item_queue_$sp.md)
- [me_01: dbo.plu_pc_queue_$sp](../../StoredProcedures/me_01/dbo.plu_pc_queue_$sp.md)
- [me_01: dbo.plu_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_regen_queue_$sp.md)
- [me_01: dbo.plu_resend_queue_$sp](../../StoredProcedures/me_01/dbo.plu_resend_queue_$sp.md)
- [me_01: dbo.plu_style_queue_$sp](../../StoredProcedures/me_01/dbo.plu_style_queue_$sp.md)
- [me_01: dbo.set_current_cost_$sp](../../StoredProcedures/me_01/dbo.set_current_cost_$sp.md)
- [me_01: dbo.upd_cancel_promo_pc_$sp](../../StoredProcedures/me_01/dbo.upd_cancel_promo_pc_$sp.md)
- [me_01: dbo.upd_promo_pc_end_date_$sp](../../StoredProcedures/me_01/dbo.upd_promo_pc_end_date_$sp.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)

