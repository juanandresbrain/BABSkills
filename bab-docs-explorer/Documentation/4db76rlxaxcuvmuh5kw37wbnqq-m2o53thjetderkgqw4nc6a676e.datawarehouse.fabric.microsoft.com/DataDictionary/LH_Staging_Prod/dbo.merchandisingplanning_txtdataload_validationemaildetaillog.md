# dbo.merchandisingplanning_txtdataload_validationemaildetaillog

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 1 |  |  |  |
| ETLBatchID | int | 4 | 1 |  |  |  |
| ETLValidationStatusID | int | 4 | 1 |  |  |  |
| MeasureName | varchar | 8000 | 1 |  |  |  |
| LocationCount | int | 4 | 1 |  |  |  |
| ProductCount | int | 4 | 1 |  |  |  |
| ValidationDateTime | datetime2 | 8 | 1 |  |  |  |
| BatchParameter_FiscalYear | int | 4 | 1 |  |  |  |
| BatchParameter_FiscalWeek | int | 4 | 1 |  |  |  |
