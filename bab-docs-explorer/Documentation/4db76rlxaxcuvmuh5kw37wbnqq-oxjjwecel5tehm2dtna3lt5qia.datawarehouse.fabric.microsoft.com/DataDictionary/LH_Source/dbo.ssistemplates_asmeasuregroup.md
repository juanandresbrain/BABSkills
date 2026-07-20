# dbo.ssistemplates_asmeasuregroup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mgID | int | 4 | 1 |  |  |  |
| cubeID | int | 4 | 1 |  |  |  |
| Descr | varchar | 8000 | 1 |  |  |  |
| normalPartitionFrequency | varchar | 8000 | 1 |  |  |  |
| numRefreshDays | int | 4 | 1 |  |  |  |
| aggregationID | varchar | 8000 | 1 |  |  |  |
| SQLText | varchar | 8000 | 1 |  |  |  |
| estimatedRows | int | 4 | 1 |  |  |  |
| ASMeasureGroup | varchar | 8000 | 1 |  |  |  |
| ASMeasureGroupID | varchar | 8000 | 1 |  |  |  |
| ASDataSourceID | varchar | 8000 | 1 |  |  |  |
| PartitionPrefix | varchar | 8000 | 1 |  |  |  |
