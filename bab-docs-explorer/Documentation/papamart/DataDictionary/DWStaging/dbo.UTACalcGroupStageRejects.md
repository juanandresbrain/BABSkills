# dbo.UTACalcGroupStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Calcgrp_ID | varchar | 50 | 1 |  |  |  |
| Calcgrp_Name | varchar | 50 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
