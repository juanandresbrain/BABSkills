# dbo.Package_BJB20240927

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PackageID | int | 4 | 0 |  |  |  |
| PackageName | varchar | -1 | 1 |  |  |  |
| Enabled | bit | 1 | 1 |  |  |  |
| IsTheme | bit | 1 | 1 |  |  |  |
| MinGuestSpend | numeric | 5 | 1 |  |  |  |
| PackageStartDate | datetime | 8 | 1 |  |  |  |
| PackageEndDate | datetime | 8 | 1 |  |  |  |
| ExecuteStartDate | datetime | 8 | 1 |  |  |  |
| ExecuteEndDate | datetime | 8 | 1 |  |  |  |
| PackageShortDesc | varchar | -1 | 1 |  |  |  |
| PackageLongDesc | varchar | -1 | 1 |  |  |  |
| EmailDescription | varchar | -1 | 1 |  |  |  |
| CountryID | int | 4 | 1 |  |  |  |
| OrderBy | int | 4 | 1 |  |  |  |

