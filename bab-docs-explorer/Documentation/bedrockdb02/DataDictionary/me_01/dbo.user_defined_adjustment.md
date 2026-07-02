# dbo.user_defined_adjustment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_defined_adjustment_id | decimal | 9 | 0 | YES |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 0 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| grouping_label | nvarchar | 90 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| submit_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| two_sided_pseudo_style_adjust | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_udt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_udt_documents_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.spMerchandisingEmailCostcoShipmentUDA](../../StoredProcedures/me_01/dbo.spMerchandisingEmailCostcoShipmentUDA.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)

