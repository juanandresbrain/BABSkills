# dbo.store_shipment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_shipment_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| from_location_id | smallint | 2 | 0 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_status | smallint | 2 | 1 |  |  |  |
| state_no | int | 4 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| ship_date | smalldatetime | 4 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| print_flag | bit | 1 | 0 |  |  |  |
| discrepancy_posted_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_store_shipment_documents_$sp](../../StoredProcedures/me_01/dbo.delete_store_shipment_documents_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.spBABWOverShort](../../StoredProcedures/me_01/dbo.spBABWOverShort.md)
- [me_01: dbo.spBABWOverShortBAK20130131](../../StoredProcedures/me_01/dbo.spBABWOverShortBAK20130131.md)
- [me_01: dbo.spMerchandising_Select_wcShipmentReceipts](../../StoredProcedures/me_01/dbo.spMerchandising_Select_wcShipmentReceipts.md)
- [me_01: dbo.spMerchandisingCompareWMtoWEBShipments](../../StoredProcedures/me_01/dbo.spMerchandisingCompareWMtoWEBShipments.md)
- [me_01: dbo.spMerchandisingEmail1DaysPastERDWarning](../../StoredProcedures/me_01/dbo.spMerchandisingEmail1DaysPastERDWarning.md)
- [me_01: dbo.spMerchandisingEmail1DaysPastERDWarning_BAK](../../StoredProcedures/me_01/dbo.spMerchandisingEmail1DaysPastERDWarning_BAK.md)
- [me_01: dbo.spMerchandisingEmail2DaysPastERDWarning](../../StoredProcedures/me_01/dbo.spMerchandisingEmail2DaysPastERDWarning.md)
- [me_01: dbo.spMerchandisingEmail2DaysPastERDWarning_BAK](../../StoredProcedures/me_01/dbo.spMerchandisingEmail2DaysPastERDWarning_BAK.md)
- [me_01: dbo.spMerchandisingEmail3DaysPastERDNotice](../../StoredProcedures/me_01/dbo.spMerchandisingEmail3DaysPastERDNotice.md)
- [me_01: dbo.spMerchandisingEmailFAOShipments](../../StoredProcedures/me_01/dbo.spMerchandisingEmailFAOShipments.md)
- [me_01: dbo.spMerchandisingEmailMacysShipments0630](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMacysShipments0630.md)
- [me_01: dbo.spMerchandisingEmailMacysShipments0631](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMacysShipments0631.md)
- [me_01: dbo.spMerchandisingEmailMacysShipments0632](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMacysShipments0632.md)
- [me_01: dbo.spMerchandisingEmailMacysShipments0633](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMacysShipments0633.md)
- [me_01: dbo.spMerchandisingEmailMacysShipments0634](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMacysShipments0634.md)
- [me_01: dbo.spMerchandisingOutputFedExReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceipts.md)
- [me_01: dbo.spMerchandisingOutputFedExReceipts_NEW20230125](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceipts_NEW20230125.md)
- [me_01: dbo.spMerchandisingOutputFedExReceiptsBAK20230125](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceiptsBAK20230125.md)
- [me_01: dbo.spMerchandisingOutputWebstoreCBR](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWebstoreCBR.md)
- [me_01: dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers.md)
- [me_01: dbo.spMerchandisingReportCartonsShippedSummary](../../StoredProcedures/me_01/dbo.spMerchandisingReportCartonsShippedSummary.md)
- [me_01: dbo.spMerchandisingReportRecType](../../StoredProcedures/me_01/dbo.spMerchandisingReportRecType.md)
- [me_01: dbo.spMerchandisingSelectCBRSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCBRSummary.md)
- [me_01: dbo.spMerchandisingSelectDDCASNSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDDCASNSummary.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentCN](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentCN.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentUK](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentUK.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentUK_BAK20220804](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentUK_BAK20220804.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentWC](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentWC.md)
- [me_01: dbo.spMerchandisingSelectShipmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShipmentSummary.md)
- [me_01: dbo.spMerchandisingSelectTransferCartons](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTransferCartons.md)
- [me_01: dbo.spMerchandisingSelectUKCartonSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKCartonSummary.md)
- [me_01: dbo.spMerchandisingSelectWMtoMerchCartonValidation](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWMtoMerchCartonValidation.md)
- [me_01: dbo.spMerchandisingSmartlookUnreceivedShipmentsReport](../../StoredProcedures/me_01/dbo.spMerchandisingSmartlookUnreceivedShipmentsReport.md)

