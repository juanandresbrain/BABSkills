# dbo.dw_monitor_databasegrowthlog

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DatabaseGrowthLogKey | int | 4 | 1 |  |  |  |
| DatabaseToMonitorGrowthKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| SizeInMB | decimal | 13 | 1 |  |  |  |
| LogTimestamp | datetime2 | 8 | 1 |  |  |  |
