# dbo.azure_customer_lead_generation

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EntryDate | datetime2 | 8 | 1 |  |  |  |
| CountryCode | varchar | 8000 | 1 |  |  |  |
| Campaign | varchar | 8000 | 1 |  |  |  |
| Source | varchar | 8000 | 1 |  |  |  |
| FileDate | date | 3 | 1 |  |  |  |
| FileName | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| customerNumber | varchar | 8000 | 1 |  |  |  |
| MembershipDate | datetime2 | 8 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| MembershipType | varchar | 8000 | 1 |  |  |  |
| isFirstEmail | int | 4 | 1 |  |  |  |
