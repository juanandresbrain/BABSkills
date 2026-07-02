# dbo.tmpWhseInventoryShrink

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| MerchQty | int | 4 | 1 |  |  |  |
| Whseqty | int | 4 | 1 |  |  |  |
| shrinkqty | int | 4 | 1 |  |  |  |
| style_type | varchar | 5 | 0 |  |  |  |
| shrinkqty_distribution_multiple | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandising_980NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_980NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandising_WEB_NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_WEB_NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandisingEmailNightlySyncReport](../../StoredProcedures/me_01/dbo.spMerchandisingEmailNightlySyncReport.md)
- [me_01: dbo.spMerchandisingEmailNightlySyncReport_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingEmailNightlySyncReport_Bak20210614.md)
- [me_01: dbo.spMerchandisingOutputWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_manual](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_manual.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801.md)

