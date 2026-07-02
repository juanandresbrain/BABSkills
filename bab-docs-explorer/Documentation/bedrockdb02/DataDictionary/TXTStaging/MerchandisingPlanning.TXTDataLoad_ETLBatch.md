# MerchandisingPlanning.TXTDataLoad_ETLBatch

**Database:** TXTStaging  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchID | int | 4 | 0 | YES |  |  |
| ETLStatusID | int | 4 | 0 |  | YES |  |
| MaxConcurrentProcess | int | 4 | 0 |  |  |  |
| ETLBatchStartDateTime | datetime | 8 | 1 |  |  |  |
| ETLBatchEndDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_StartFiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_StartFiscalWeek | int | 4 | 1 |  |  |  |
| BatchParameter_EndFiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_EndFiscalWeek | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Report_CurrentBatch](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Report_CurrentBatch.md)

