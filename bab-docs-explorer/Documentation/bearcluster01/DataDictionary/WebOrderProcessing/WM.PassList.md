# WM.PassList

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PassListID | int | 4 | 0 | YES |  |  |
| PassListWord | varchar | 100 | 0 |  |  |  |
| CRTED_BY | varchar | 255 | 1 |  |  |  |
| CRTED_ON | datetime | 8 | 0 |  |  |  |
| UPDTD_BY | varchar | 255 | 1 |  |  |  |
| UPDTD_ON | datetime | 8 | 0 |  |  |  |
| BlackListID | int | 4 | 0 |  | YES |  |

