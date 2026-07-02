# MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog_2

**Database:** USICOAL  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchDetailLogID | int | 4 | 0 |  |  |  |
| ETLBatchID | int | 4 | 0 |  |  |  |
| ETLStatusID | int | 4 | 0 |  |  |  |
| StatementWithoutParameter | nvarchar | 8000 | 0 |  |  |  |
| ETLBatchDetailItemStartDateTime | datetime | 8 | 1 |  |  |  |
| ETLBatchDetailItemEndDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_FiscalWeek | nvarchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLogV2_UpdateBatchStatus](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLogV2_UpdateBatchStatus.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Report_CurrentBatch](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Report_CurrentBatch.md)

