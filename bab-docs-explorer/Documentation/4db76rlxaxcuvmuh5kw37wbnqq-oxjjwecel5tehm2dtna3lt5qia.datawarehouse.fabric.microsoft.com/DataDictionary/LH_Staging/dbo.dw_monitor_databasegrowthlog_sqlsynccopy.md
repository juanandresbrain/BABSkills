# dbo.dw_monitor_databasegrowthlog_sqlsynccopy

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DatabaseGrowthLogKey | int | 4 | 1 |  |  |  |
| DatabaseToMonitorGrowthKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| SizeInMB | decimal | 13 | 1 |  |  |  |
| LogTimestamp | datetime2 | 8 | 1 |  |  |  |
