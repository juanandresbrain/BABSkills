# dbo.wm_vworderstatuspivot

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| CurrentStatus | varchar | 8000 | 1 |  |  |  |
| PendingStatusDate | datetime2 | 8 | 1 |  |  |  |
| WavedStatusDate | datetime2 | 8 | 1 |  |  |  |
| ShippedCompletedStatusDate | datetime2 | 8 | 1 |  |  |  |
