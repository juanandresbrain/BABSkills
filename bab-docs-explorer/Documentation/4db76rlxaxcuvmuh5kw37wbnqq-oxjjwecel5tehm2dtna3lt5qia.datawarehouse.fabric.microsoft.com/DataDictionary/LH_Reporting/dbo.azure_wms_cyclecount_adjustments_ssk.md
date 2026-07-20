# dbo.azure_wms_cyclecount_adjustments_ssk

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DateOfCount | date | 3 | 1 |  |  |  |
| ApprovedDate | date | 3 | 1 |  |  |  |
| Location | varchar | 8000 | 1 |  |  |  |
| Warehouse | varchar | 8000 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| CounterId | varchar | 8000 | 1 |  |  |  |
| ApproverId | varchar | 8000 | 1 |  |  |  |
| FinalCountAmt | float | 8 | 1 |  |  |  |
| AmtBeforeCount | float | 8 | 1 |  |  |  |
| UnitDifference | float | 8 | 1 |  |  |  |
| DollarDifference | float | 8 | 1 |  |  |  |
