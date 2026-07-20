# dbo.merchandisingplanning_txtdataload_etlbatch

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchID | int | 4 | 1 |  |  |  |
| ETLStatusID | int | 4 | 1 |  |  |  |
| MaxConcurrentProcess | int | 4 | 1 |  |  |  |
| ETLBatchStartDateTime | datetime2 | 8 | 1 |  |  |  |
| ETLBatchEndDateTime | datetime2 | 8 | 1 |  |  |  |
| BatchParameter_StartFiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_StartFiscalWeek | int | 4 | 1 |  |  |  |
| BatchParameter_EndFiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_EndFiscalWeek | int | 4 | 1 |  |  |  |
