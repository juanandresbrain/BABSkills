# dbo.shrink_adjustment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shrink_adjustment_id | decimal | 9 | 0 | YES |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| submit_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| shrink_type | smallint | 2 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_shrink_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_shrink_adj_documents_$sp.md)
- [me_01: dbo.spMerchandisingNightlySyncPostSummary](../../StoredProcedures/me_01/dbo.spMerchandisingNightlySyncPostSummary.md)
- [me_01: dbo.spMerchandisingOutputUKstoreMHUshrink](../../StoredProcedures/me_01/dbo.spMerchandisingOutputUKstoreMHUshrink.md)
- [me_01: dbo.spMerchandisingSelectMultipleShrinkDocs](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMultipleShrinkDocs.md)
- [me_01: dbo.spMerchandisingSelectShrinkAdjustmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkAdjustmentSummary.md)

