# dbo.UTAProjectStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Proj_ID | bigint | 8 | 1 |  |  |  |
| Proj_Name | varchar | 40 | 1 |  |  |  |
| Proj_Desc | varchar | 100 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
