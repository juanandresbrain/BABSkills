# dbo.Line_Object_Action_Master

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| target | varchar | 10 | 0 |  |  |  |
| factor | smallint | 2 | 0 |  |  |  |
| needsReview | bit | 1 | 0 |  |  | This record needs to be reviewed. It is a new record from Auditworks |
| dontAllocationTo | bit | 1 | 0 |  |  | TDF only. Do not allocate discounts to this record |
| needsAllocation | bit | 1 | 0 |  |  | This line object/action will need to be allocated as a part the import process. This appears on a DISC destination. |
