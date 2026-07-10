# dbo.UTAWorkSummaryStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| wrks_id | varchar | 50 | 1 |  |  |  |
| emp_id | varchar | 50 | 1 |  |  |  |
| wrks_work_date | varchar | 50 | 1 |  |  |  |
| paygrp_id | varchar | 50 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
