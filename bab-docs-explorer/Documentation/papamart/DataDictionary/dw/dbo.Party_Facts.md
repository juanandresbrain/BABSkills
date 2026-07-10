# dbo.Party_Facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| party_key | int | 4 | 0 | YES |  |  |
| PartyID | int | 4 | 0 |  |  |  |
| OccasionName | varchar | 128 | 1 |  |  |  |
| ThemeName | nvarchar | 200 | 1 |  |  |  |
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
| INS_DT | datetime | 8 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| PMRNumber | int | 4 | 1 |  |  |  |
