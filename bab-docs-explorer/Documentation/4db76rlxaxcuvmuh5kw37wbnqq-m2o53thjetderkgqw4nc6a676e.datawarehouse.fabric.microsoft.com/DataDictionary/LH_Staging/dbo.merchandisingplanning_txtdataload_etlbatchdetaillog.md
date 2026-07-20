# dbo.merchandisingplanning_txtdataload_etlbatchdetaillog

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchDetailLogID | int | 4 | 1 |  |  |  |
| ETLBatchID | int | 4 | 1 |  |  |  |
| ETLStatusID | int | 4 | 1 |  |  |  |
| StatementWithoutParameter | varchar | 8000 | 1 |  |  |  |
| ETLBatchDetailItemStartDateTime | datetime2 | 8 | 1 |  |  |  |
| ETLBatchDetailItemEndDateTime | datetime2 | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_FiscalWeek | int | 4 | 1 |  |  |  |
