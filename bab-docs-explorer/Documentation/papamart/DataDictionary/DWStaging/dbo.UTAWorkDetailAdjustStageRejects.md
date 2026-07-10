# dbo.UTAWorkDetailAdjustStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Wbt_ID | varchar | 50 | 1 |  |  |  |
| Wrkda_Work_Date | varchar | 50 | 1 |  |  |  |
| Htype_ID | varchar | 50 | 1 |  |  |  |
| WRKDA_ID | varchar | 50 | 1 |  |  |  |
| wrkda_minutes | varchar | 50 | 1 |  |  |  |
| tcode_id | varchar | 50 | 1 |  |  |  |
| wrkda_adjust_date | varchar | 50 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
| proj_id | bigint | 8 | 1 |  |  |  |
