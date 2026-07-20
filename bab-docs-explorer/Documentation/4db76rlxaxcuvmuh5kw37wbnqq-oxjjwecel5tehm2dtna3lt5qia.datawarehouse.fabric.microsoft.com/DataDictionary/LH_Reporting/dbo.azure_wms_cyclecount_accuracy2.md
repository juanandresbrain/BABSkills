# dbo.azure_wms_cyclecount_accuracy2

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AmtBeforeCount | float | 8 | 1 |  |  |  |
| DateOfCount | date | 3 | 1 |  |  |  |
| FinalCountAmt | float | 8 | 1 |  |  |  |
| Location | varchar | 8000 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| UnitDifference | float | 8 | 1 |  |  |  |
| DollarDifference | float | 8 | 1 |  |  |  |
| PerpetualDollarAmt | float | 8 | 1 |  |  |  |
| UnitDifferencePerc | float | 8 | 1 |  |  |  |
| Warehouse | varchar | 8000 | 1 |  |  |  |
