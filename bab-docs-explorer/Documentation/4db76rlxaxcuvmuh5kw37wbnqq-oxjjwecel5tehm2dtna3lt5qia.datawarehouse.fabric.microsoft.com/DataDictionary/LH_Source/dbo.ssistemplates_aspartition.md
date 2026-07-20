# dbo.ssistemplates_aspartition

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| partID | int | 4 | 1 |  |  |  |
| mgID | int | 4 | 1 |  |  |  |
| SSASPartitionName | varchar | 8000 | 1 |  |  |  |
| fromDate_Key | int | 4 | 1 |  |  |  |
| thruDate_Key | int | 4 | 1 |  |  |  |
| aggregationID | varchar | 8000 | 1 |  |  |  |
| SQLText | varchar | 8000 | 1 |  |  |  |
| estimatedRows | int | 4 | 1 |  |  |  |
| PartitionSlice | varchar | 8000 | 1 |  |  |  |
| createdDt | datetime2 | 8 | 1 |  |  |  |
