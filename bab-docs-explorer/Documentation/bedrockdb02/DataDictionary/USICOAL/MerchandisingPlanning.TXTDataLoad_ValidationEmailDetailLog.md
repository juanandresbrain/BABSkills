# MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog

**Database:** USICOAL  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 |  |  |  |
| ETLBatchID | int | 4 | 0 |  |  |  |
| ETLValidationStatusID | int | 4 | 0 |  |  |  |
| MeasureName | nvarchar | 1000 | 0 |  |  |  |
| LocationCount | int | 4 | 0 |  |  |  |
| ProductCount | int | 4 | 1 |  |  |  |
| ValidationDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 0 |  |  |  |
| BatchParameter_FiscalWeek | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Inv Ch Tfr Cost Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Cost_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Inv Ch Tfr Unit_SingleFiscalWeek_Value_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Unit_SingleFiscalWeek_Value_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Inv Ch Tfr Value_SingleFiscalWeek_Value_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Value_SingleFiscalWeek_Value_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Inv EOP Cost Value_SingleFiscalWeek_Value_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Cost_Value_SingleFiscalWeek_Value_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Inv EOP Unit_SingleFiscalWeek_Value_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Unit_SingleFiscalWeek_Value_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Inv EOP Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Markdown Perm Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Markdown_Perm_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Markdown POS Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Markdown_POS_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs On Order Cost Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Cost_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs On Order Unit_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Unit_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs On Order Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Receipts Cost Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Cost_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Receipts Unit_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Unit_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Receipts Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Sales Cost Value Base_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Cost_Value_Base_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Sales Unit_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Unit_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Sales Value Base_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Value_Base_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Sales Value Local_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Value_Local_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Shrink Cost Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Cost_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Shrink Unit_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Unit_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Shrink Value_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Value_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Store Count_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Count_SingleFiscalWeek_Validation.md)
- [ma_01: MerchandisingPlanning.spTXTDataLoad_Measure_hs Store Status_SingleFiscalWeek_Validation](../../StoredProcedures/ma_01/MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Status_SingleFiscalWeek_Validation.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_Coordinator_BAK.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation.md)

