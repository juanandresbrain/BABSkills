# dbo.PartyFacts_Staging

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyID | int | 4 | 1 |  |  |  |
| OccasionName | varchar | 128 | 1 |  |  |  |
| PackageName | varchar | -1 | 1 |  |  |  |
| TotalGuests | int | 4 | 1 |  |  |  |
| GOHAge | int | 4 | 1 |  |  |  |
| GuestAvgAge | int | 4 | 1 |  |  |  |
| IsCancelled | bit | 1 | 1 |  |  |  |
| IsPOParty | bit | 1 | 1 |  |  |  |
| CreatedDateKey | int | 4 | 1 |  |  |  |
| ExecuteDateKey | int | 4 | 1 |  |  |  |
| ExecuteTimeKey | int | 4 | 1 |  |  |  |
| CreatedBy | varchar | 128 | 1 |  |  |  |
| BookingMethod | varchar | 3 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |

