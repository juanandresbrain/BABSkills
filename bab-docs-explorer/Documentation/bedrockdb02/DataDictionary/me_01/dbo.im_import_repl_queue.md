# dbo.im_import_repl_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| im_import_repl_queue_id | decimal | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | nvarchar | 4 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_key | nvarchar | 40 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandising_980NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_980NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandising_WEB_NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_WEB_NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandisingEmailImportUDAerrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailImportUDAerrors.md)
- [me_01: dbo.spMerchandisingEmailShipmentErrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailShipmentErrors.md)
- [me_01: dbo.spMerchandisingNightlySyncPostSummary](../../StoredProcedures/me_01/dbo.spMerchandisingNightlySyncPostSummary.md)
- [me_01: dbo.spMerchandisingReportPOReceiptErrors](../../StoredProcedures/me_01/dbo.spMerchandisingReportPOReceiptErrors.md)
- [me_01: dbo.spMerchandisingSelectCBRSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCBRSummary.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)
- [me_01: dbo.spMerchandisingSelectShipmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShipmentSummary.md)
- [me_01: dbo.spMerchandisingSelectShrinkAdjustmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkAdjustmentSummary.md)
- [me_01: dbo.spMerchandisingSelectShrinkErrors](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkErrors.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_manual](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_manual.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801.md)

