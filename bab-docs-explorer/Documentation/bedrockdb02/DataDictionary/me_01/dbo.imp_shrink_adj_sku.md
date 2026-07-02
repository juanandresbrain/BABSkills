# dbo.imp_shrink_adj_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_shrink_adj_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_shrink_adj_id | decimal | 9 | 1 |  |  |  |
| action | char | 1 | 0 |  |  |  |
| document_no | varchar | 20 | 0 |  |  |  |
| location_code | varchar | 20 | 0 |  |  |  |
| upc_number | varchar | 14 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| primary_size_label | varchar | 8 | 1 |  |  |  |
| secondary_size_label | varchar | 8 | 1 |  |  |  |
| units_to_adjust | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandising_980NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_980NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandising_WEB_NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_WEB_NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandisingNightlySyncPostSummary](../../StoredProcedures/me_01/dbo.spMerchandisingNightlySyncPostSummary.md)
- [me_01: dbo.spMerchandisingSelectShrinkAdjustmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkAdjustmentSummary.md)
- [me_01: dbo.spMerchandisingSelectShrinkErrors](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkErrors.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_manual](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_manual.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801.md)

