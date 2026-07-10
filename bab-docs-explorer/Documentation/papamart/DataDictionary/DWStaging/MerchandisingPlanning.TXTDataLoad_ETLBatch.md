# MerchandisingPlanning.TXTDataLoad_ETLBatch

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchID | int | 4 | 0 | YES |  |  |
| ETLStatusID | int | 4 | 0 |  |  |  |
| MaxConcurrentProcess | int | 4 | 0 |  |  |  |
| ETLBatchStartDateTime | datetime | 8 | 1 |  |  |  |
| ETLBatchEndDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_StartFiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_StartFiscalWeek | int | 4 | 1 |  |  |  |
| BatchParameter_EndFiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_EndFiscalWeek | int | 4 | 1 |  |  |  |
