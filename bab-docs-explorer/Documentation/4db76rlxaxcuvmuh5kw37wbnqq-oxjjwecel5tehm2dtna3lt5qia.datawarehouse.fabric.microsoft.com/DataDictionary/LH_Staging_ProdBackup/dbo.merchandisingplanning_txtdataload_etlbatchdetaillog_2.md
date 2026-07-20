# dbo.merchandisingplanning_txtdataload_etlbatchdetaillog_2

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
| BatchParameter_FiscalWeek | varchar | 8000 | 1 |  |  |  |
