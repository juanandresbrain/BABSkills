# MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK

**Database:** TXTStaging  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_AsyncExecute(["MerchandisingPlanning.spTXTDataLoad_AsyncExecute"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_CleanseFailedMeasures(["MerchandisingPlanning.spTXTDataLoad_CleanseFailedMeasures"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_CompletionFile(["MerchandisingPlanning.spTXTDataLoad_CompletionFile"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_ETLBatch_EmailReport(["MerchandisingPlanning.spTXTDataLoad_ETLBatch_EmailReport"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_ETLBatch_UpdateBatchStatus(["MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus(["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation(["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_ETLBatchDetailLogV2_UpdateBatchStatus(["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLogV2_UpdateBatchStatus"]) --> SP
    MerchandisingPlanning_spTXTDataLoad_SetFailedBit(["MerchandisingPlanning.spTXTDataLoad_SetFailedBit"]) --> SP
    MerchandisingPlanning_TXTDataLoad_ETLBatch(["MerchandisingPlanning.TXTDataLoad_ETLBatch"]) --> SP
    MerchandisingPlanning_TXTDataLoad_ETLBatchDetailLog(["MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog"]) --> SP
    MerchandisingPlanning_TXTDataLoad_ETLBatchDetailLog_2(["MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog_2"]) --> SP
    MerchandisingPlanning_TXTDataLoad_Measure_StoredProcedureListInOrder(["MerchandisingPlanning.TXTDataLoad_Measure_StoredProcedureListInOrder"]) --> SP
    MerchandisingPlanning_TXTDataLoad_Measure_StoredProcedureListInOrder_2(["MerchandisingPlanning.TXTDataLoad_Measure_StoredProcedureListInOrder_2"]) --> SP
    MerchandisingPlanning_TXTDataLoad_Measure_StoredProcedureListInOrder_Validation(["MerchandisingPlanning.TXTDataLoad_Measure_StoredProcedureListInOrder_Validation"]) --> SP
    MerchandisingPlanning_TXTDataLoad_ValidationEmailDetailLog(["MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog"]) --> SP
    MerchandisingPlanning_vwTXT_CalculatedTime(["MerchandisingPlanning.vwTXT_CalculatedTime"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |
| MerchandisingPlanning.spTXTDataLoad_AsyncExecute |
| MerchandisingPlanning.spTXTDataLoad_CleanseFailedMeasures |
| MerchandisingPlanning.spTXTDataLoad_CompletionFile |
| MerchandisingPlanning.spTXTDataLoad_ETLBatch_EmailReport |
| MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus |
| MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation |
| MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLogV2_UpdateBatchStatus |
| MerchandisingPlanning.spTXTDataLoad_SetFailedBit |
| MerchandisingPlanning.TXTDataLoad_ETLBatch |
| MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog |
| MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog_2 |
| MerchandisingPlanning.TXTDataLoad_Measure_StoredProcedureListInOrder |
| MerchandisingPlanning.TXTDataLoad_Measure_StoredProcedureListInOrder_2 |
| MerchandisingPlanning.TXTDataLoad_Measure_StoredProcedureListInOrder_Validation |
| MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning.vwTXT_CalculatedTime |

## Stored Procedure Code

```sql

```

