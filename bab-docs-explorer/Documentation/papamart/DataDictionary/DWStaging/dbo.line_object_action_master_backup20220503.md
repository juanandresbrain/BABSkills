# dbo.line_object_action_master_backup20220503

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| target | varchar | 10 | 0 |  |  |  |
| factor | smallint | 2 | 0 |  |  |  |
| needsReview | bit | 1 | 0 |  |  |  |
| dontAllocationTo | bit | 1 | 0 |  |  |  |
| needsAllocation | bit | 1 | 0 |  |  |  |
