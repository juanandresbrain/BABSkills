# dbo.extension_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| extension_queue_id | bigint | 8 | 0 | YES |  |  |
| type | smallint | 2 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| method_id | nvarchar | 80 | 0 |  |  |  |
| entity_name | nvarchar | 120 | 0 |  |  |  |
| action | nvarchar | 60 | 1 |  |  |  |
| message | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)
- [me_01: dbo.set_current_cost_$sp](../../StoredProcedures/me_01/dbo.set_current_cost_$sp.md)

