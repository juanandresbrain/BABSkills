# dbo.weborderprocessing_wm_orderstatus

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderStatusId | int | 4 | 1 |  |  |  |
| OrderId | int | 4 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| StatusDate | datetime2 | 8 | 1 |  |  |  |
| CurrentStatus | bit | 1 | 1 |  |  |  |
