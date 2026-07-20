# dbo.line_object_action_master

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | int | 4 | 1 |  |  |  |
| line_action | int | 4 | 1 |  |  |  |
| target | varchar | 8000 | 1 |  |  |  |
| factor | int | 4 | 1 |  |  |  |
| needsReview | bit | 1 | 1 |  |  |  |
| dontAllocationTo | bit | 1 | 1 |  |  |  |
| needsAllocation | bit | 1 | 1 |  |  |  |
