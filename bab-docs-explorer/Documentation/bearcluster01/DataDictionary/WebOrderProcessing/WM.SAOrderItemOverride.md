# WM.SAOrderItemOverride

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SAOrderItemOverrideId | int | 4 | 0 | YES |  |  |
| OriginalSku | varchar | 50 | 0 |  |  |  |
| OverrideSku | varchar | 50 | 0 |  |  |  |
| OverrideDescription | varchar | -1 | 1 |  |  |  |
| OverrideStartDate | date | 3 | 0 |  |  |  |
| OverrideEndDate | date | 3 | 0 |  |  |  |
| OverrideRangeId | int | 4 | 0 |  |  |  |
| RangeId | int | 4 | 0 |  |  |  |

