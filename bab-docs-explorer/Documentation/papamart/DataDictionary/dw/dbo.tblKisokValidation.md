# dbo.tblKisokValidation

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| iRecordCount | int | 4 | 1 |  |  |  |
| dStartDate | datetime | 8 | 1 |  |  |  |
| dEndDate | datetime | 8 | 1 |  |  |  |
| sTblName | varchar | 18 | 0 |  |  |  |
| iStoreID | int | 4 | 1 |  |  |  |
| itblKioskValID | int | 4 | 0 | YES |  |  |
