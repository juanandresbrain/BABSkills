# dbo.SFSPointsCRMDetail

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditPeriodKey | smallint | 2 | 0 |  |  |  |
| CustomerID | int | 4 | 0 |  |  |  |
| CountryCode | varchar | 3 | 0 |  |  |  |
| CustomerNumber | numeric | 13 | 0 |  |  |  |
| InDW | char | 1 | 0 |  |  |  |
| Tier | float | 8 | 0 |  |  |  |
| TotalCurrentPoints | numeric | 9 | 1 |  |  |  |
| LastDatePointsPosted | smalldatetime | 4 | 1 |  |  |  |
| DaysOld | int | 4 | 1 |  |  |  |
| PointsGroup | varchar | 19 | 0 |  |  |  |
| LastPostedGroup | varchar | 14 | 0 |  |  |  |
