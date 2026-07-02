# MerchandisingPlanning.spTXTDataLoad_Measure_hs On Order Unit_SingleFiscalWeek_V2

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_Measure_hs On Order Unit_SingleFiscalWeek_V2"]
    MerchandisingPlanning_spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2(["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2"]) --> SP
    MerchandisingPlanning_vwTXT_CalculatedTime(["MerchandisingPlanning.vwTXT_CalculatedTime"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning.vwTXT_CalculatedTime |

## Stored Procedure Code

```sql

```

