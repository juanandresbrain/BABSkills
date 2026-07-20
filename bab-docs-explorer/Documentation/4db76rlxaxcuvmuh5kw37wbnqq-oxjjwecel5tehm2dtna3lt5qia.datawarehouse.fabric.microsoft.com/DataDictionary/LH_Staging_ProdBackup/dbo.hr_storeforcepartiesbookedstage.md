# dbo.hr_storeforcepartiesbookedstage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| PartyBookDate | varchar | 8000 | 1 |  |  |  |
| Slot | varchar | 8000 | 1 |  |  |  |
| PartiesBooked | int | 4 | 1 |  |  |  |
| StoreIDRaw | int | 4 | 1 |  |  |  |
| PartyBookDateRaw | date | 3 | 1 |  |  |  |
