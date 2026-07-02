# dbo.season

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| season_id | smallint | 2 | 0 | YES |  |  |
| season_code | nvarchar | 4 | 0 |  |  |  |
| season_description | nvarchar | 80 | 0 |  |  |  |
| year_required_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_store_shipment_$sp](../../StoredProcedures/me_01/dbo.rpt_get_store_shipment_$sp.md)
- [me_01: dbo.rpt_get_unsolicited_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_unsolicited_receipt_$sp.md)
- [me_01: dbo.spMerchandisingReportRoyaltyUpdates](../../StoredProcedures/me_01/dbo.spMerchandisingReportRoyaltyUpdates.md)
- [me_01: dbo.spMerchandisingReportStyleList](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList.md)
- [me_01: dbo.spMerchandisingReportStyleList_BU20200513](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList_BU20200513.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [USICOAL: dbo.DC_CHK_ITM_REF_INTGR](../../StoredProcedures/USICOAL/dbo.DC_CHK_ITM_REF_INTGR.md)
- [USICOAL: dbo.DC_INS_ITEM](../../StoredProcedures/USICOAL/dbo.DC_INS_ITEM.md)
- [USICOAL: dbo.DC_RPL_ITEM](../../StoredProcedures/USICOAL/dbo.DC_RPL_ITEM.md)
- [USICOAL: dbo.DC_RPL_PLU](../../StoredProcedures/USICOAL/dbo.DC_RPL_PLU.md)
- [USICOAL: dbo.DC_UPD_ITEM](../../StoredProcedures/USICOAL/dbo.DC_UPD_ITEM.md)

