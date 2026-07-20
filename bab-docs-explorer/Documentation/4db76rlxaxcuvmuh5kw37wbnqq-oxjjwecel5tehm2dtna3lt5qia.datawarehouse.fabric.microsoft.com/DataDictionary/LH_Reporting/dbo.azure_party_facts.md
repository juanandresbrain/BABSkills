# dbo.azure_party_facts

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| party_key | int | 4 | 1 |  |  |  |
| OccasionName | varchar | 8000 | 1 |  |  |  |
| PackageName | varchar | 8000 | 1 |  |  |  |
| TotalGuests | int | 4 | 1 |  |  |  |
| GOHAge | int | 4 | 1 |  |  |  |
| GuestAvgAge | int | 4 | 1 |  |  |  |
| IsCancelled | bit | 1 | 1 |  |  |  |
| IsPOParty | bit | 1 | 1 |  |  |  |
| CreatedDate | datetime2 | 8 | 1 |  |  |  |
| ExecuteDate | datetime2 | 8 | 1 |  |  |  |
| CreatedBy | varchar | 8000 | 1 |  |  |  |
| BookingMethod | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
