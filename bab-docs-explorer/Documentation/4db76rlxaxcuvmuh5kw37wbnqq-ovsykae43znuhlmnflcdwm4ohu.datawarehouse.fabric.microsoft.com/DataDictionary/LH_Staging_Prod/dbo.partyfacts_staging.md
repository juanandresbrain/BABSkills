# dbo.partyfacts_staging

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyID | int | 4 | 1 |  |  |  |
| OccasionName | varchar | 8000 | 1 |  |  |  |
| PackageName | varchar | 8000 | 1 |  |  |  |
| TotalGuests | int | 4 | 1 |  |  |  |
| GOHAge | int | 4 | 1 |  |  |  |
| GuestAvgAge | int | 4 | 1 |  |  |  |
| IsCancelled | bit | 1 | 1 |  |  |  |
| IsPOParty | bit | 1 | 1 |  |  |  |
| CreatedDateKey | int | 4 | 1 |  |  |  |
| ExecuteDateKey | int | 4 | 1 |  |  |  |
| ExecuteTimeKey | int | 4 | 1 |  |  |  |
| CreatedBy | varchar | 8000 | 1 |  |  |  |
| BookingMethod | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| PMRNumber | int | 4 | 1 |  |  |  |
| ThemeName | varchar | 8000 | 1 |  |  |  |
