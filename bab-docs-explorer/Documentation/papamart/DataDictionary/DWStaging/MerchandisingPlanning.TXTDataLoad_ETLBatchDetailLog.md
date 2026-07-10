# MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETLBatchDetailLogID | int | 4 | 0 | YES |  |  |
| ETLBatchID | int | 4 | 0 |  |  |  |
| ETLStatusID | int | 4 | 0 |  |  |  |
| StatementWithoutParameter | nvarchar | 8000 | 0 |  |  |  |
| ETLBatchDetailItemStartDateTime | datetime | 8 | 1 |  |  |  |
| ETLBatchDetailItemEndDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_FiscalWeek | int | 4 | 1 |  |  |  |
