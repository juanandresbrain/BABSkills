# MerchandisingPlanning.spTXTDataLoad_Measure_hs Sales Cost Value Base_SingleFiscalWeek_Validation

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_Measure_hs Sales Cost Value Base_SingleFiscalWeek_Validation"]
    MerchandisingPlanning_spTXTDataLoad_ETLBatchDetailLog_UpdateValidation(["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation"]) --> SP
    MerchandisingPlanning_TXTDataLoad_ValidationEmailDetailLog(["MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation |
| MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |

## Stored Procedure Code

```sql

```

