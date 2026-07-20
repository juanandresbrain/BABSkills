# dbo.hr_storeforcepartiesbookedstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| PartyBookDate | varchar | 8000 | 1 |  |  |  |
| Slot | varchar | 8000 | 1 |  |  |  |
| PartiesBooked | int | 4 | 1 |  |  |  |
| StoreIDRaw | int | 4 | 1 |  |  |  |
| PartyBookDateRaw | date | 3 | 1 |  |  |  |
