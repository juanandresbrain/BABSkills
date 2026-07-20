# dbo.sfspointscrmdetail

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditPeriodKey | int | 4 | 1 |  |  |  |
| CustomerID | int | 4 | 1 |  |  |  |
| CountryCode | varchar | 8000 | 1 |  |  |  |
| CustomerNumber | decimal | 13 | 1 |  |  |  |
| InDW | varchar | 8000 | 1 |  |  |  |
| Tier | float | 8 | 1 |  |  |  |
| TotalCurrentPoints | decimal | 9 | 1 |  |  |  |
| LastDatePointsPosted | datetime2 | 8 | 1 |  |  |  |
| DaysOld | int | 4 | 1 |  |  |  |
| PointsGroup | varchar | 8000 | 1 |  |  |  |
| LastPostedGroup | varchar | 8000 | 1 |  |  |  |
