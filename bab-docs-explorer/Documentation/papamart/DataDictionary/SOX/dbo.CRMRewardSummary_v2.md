# dbo.CRMRewardSummary_v2

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditPeriodKey | smallint | 2 | 0 |  |  |  |
| CountryCode | varchar | 3 | 0 |  |  |  |
| BeginningPointsTotal | int | 4 | 1 |  |  |  |
| EarnedPointsTotal | int | 4 | 1 |  |  |  |
| RedeemedPointsTotal | int | 4 | 1 |  |  |  |
| AdjustedPointsTotal | int | 4 | 1 |  |  |  |
| ExpiredPointsTotal | int | 4 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
| InsertUser | varchar | 50 | 1 |  |  |  |
| UpdateDate | date | 3 | 1 |  |  |  |
| UpdateUser | varchar | 50 | 1 |  |  |  |
