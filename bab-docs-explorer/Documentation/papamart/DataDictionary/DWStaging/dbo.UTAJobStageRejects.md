# dbo.UTAJobStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JOB_ID | varchar | 50 | 1 |  |  |  |
| JOB_NAME | varchar | 50 | 1 |  |  |  |
| JOB_DESC | varchar | 100 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
