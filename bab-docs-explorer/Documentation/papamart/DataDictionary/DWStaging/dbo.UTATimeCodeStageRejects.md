# dbo.UTATimeCodeStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TCODE_ID | varchar | 50 | 1 |  |  |  |
| TCODE_NAME | varchar | 50 | 1 |  |  |  |
| TCODE_DESC | varchar | 100 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
