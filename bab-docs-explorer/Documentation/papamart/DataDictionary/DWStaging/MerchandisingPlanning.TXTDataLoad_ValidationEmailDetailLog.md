# MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ETLBatchID | int | 4 | 0 |  |  |  |
| ETLValidationStatusID | int | 4 | 0 |  |  |  |
| MeasureName | nvarchar | 1000 | 0 |  |  |  |
| LocationCount | int | 4 | 0 |  |  |  |
| ProductCount | int | 4 | 1 |  |  |  |
| ValidationDateTime | datetime | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 0 |  |  |  |
| BatchParameter_FiscalWeek | int | 4 | 0 |  |  |  |
