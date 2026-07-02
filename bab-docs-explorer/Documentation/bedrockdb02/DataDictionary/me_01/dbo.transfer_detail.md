# dbo.transfer_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transfer_detail_id | decimal | 9 | 0 | YES |  |  |
| transfer_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| units_received | int | 4 | 1 |  |  |  |
| units_sent | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dant_DamageTransfersWithoutCartonNumbers](../../StoredProcedures/me_01/dbo.dant_DamageTransfersWithoutCartonNumbers.md)
- [me_01: dbo.delete_transfer_documents_$sp](../../StoredProcedures/me_01/dbo.delete_transfer_documents_$sp.md)
- [me_01: dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers.md)
- [me_01: dbo.spMerchandisingProcessWcStockAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWcStockAdj.md)
- [me_01: dbo.spMerchandisingSelectCAPOCBR](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCAPOCBR.md)
- [me_01: dbo.spMerchandisingSelectCBRSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCBRSummary.md)
- [me_01: dbo.spMerchandisingSelectPoolPointTransferReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPoolPointTransferReceipts.md)
- [me_01: dbo.spMerchandisingSelectTransferCartons](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTransferCartons.md)
- [me_01: dbo.spMerchandisingSelectUKPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKPOReceipts.md)
- [me_01: dbo.spMerchandisingSelectUnreceivedTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUnreceivedTransfers.md)
- [me_01: dbo.spMerchandisingTransferImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingTransferImportValidation.md)
- [me_01: dbo.xfers_from_distro_$sp](../../StoredProcedures/me_01/dbo.xfers_from_distro_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

