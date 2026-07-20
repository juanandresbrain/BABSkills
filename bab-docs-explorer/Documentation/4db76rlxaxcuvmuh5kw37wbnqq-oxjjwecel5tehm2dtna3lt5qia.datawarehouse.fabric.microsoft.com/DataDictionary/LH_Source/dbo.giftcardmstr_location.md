# dbo.giftcardmstr_location

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationID | int | 4 | 1 |  |  |  |
| VendorID | int | 4 | 1 |  |  |  |
| BABWLocationCode | varchar | 8000 | 1 |  |  |  |
| VendorLocationNumber | varchar | 8000 | 1 |  |  |  |
| LocationName | varchar | 8000 | 1 |  |  |  |
| LocationAddress1 | varchar | 8000 | 1 |  |  |  |
| LocationAddress2 | varchar | 8000 | 1 |  |  |  |
| LocationCity | varchar | 8000 | 1 |  |  |  |
| LocationState | varchar | 8000 | 1 |  |  |  |
| LocationZip | varchar | 8000 | 1 |  |  |  |
| LocationCountryID | int | 4 | 1 |  |  |  |
| LocationContact | varchar | 8000 | 1 |  |  |  |
| LocationDivision | varchar | 8000 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_DT | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_DT | datetime2 | 8 | 1 |  |  |  |
