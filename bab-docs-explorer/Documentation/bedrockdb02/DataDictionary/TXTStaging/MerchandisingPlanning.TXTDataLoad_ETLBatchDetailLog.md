# MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog

**Database:** TXTStaging  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchDetailLogID | int | 4 | 0 | YES |  |  |
| ETLBatchID | int | 4 | 0 |  | YES |  |
| ETLBatchID | int | 4 | 0 |  | YES |  |
| ETLStatusID | int | 4 | 0 |  | YES |  |
| ETLStatusID | int | 4 | 0 |  | YES |  |
| StatementWithoutParameter | nvarchar | 8000 | 0 |  |  |  |
| ETLBatchDetailItemStartDateTime | datetime | 8 | 1 |  |  |  |
| ETLBatchDetailItemEndDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_FiscalWeek | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Report_CurrentBatch](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Report_CurrentBatch.md)

