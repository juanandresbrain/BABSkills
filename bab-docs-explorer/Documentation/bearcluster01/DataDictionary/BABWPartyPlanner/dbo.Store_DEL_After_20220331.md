# dbo.Store_DEL_After_20220331

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 0 |  |  |  |
| MinutesBetweenParties | int | 4 | 1 |  |  |  |
| BookingParties | bit | 1 | 1 |  |  |  |
| WebMessage | varchar | 8000 | 1 |  |  |  |
| BSRMessage | varchar | 8000 | 1 |  |  |  |
| ParentStore | int | 4 | 1 |  |  |  |
| CancellationHours | int | 4 | 1 |  |  |  |
| ModificationDays | int | 4 | 1 |  |  |  |
| MinGuests | int | 4 | 1 |  |  |  |
| MaxGuests | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| DefaultStartOffset | int | 4 | 1 |  |  |  |
| DefaultEndOffset | int | 4 | 1 |  |  |  |
| StoreGroupID | int | 4 | 1 |  |  |  |
| CountryID | int | 4 | 1 |  |  |  |
| CanBookOnline | bit | 1 | 1 |  |  |  |

