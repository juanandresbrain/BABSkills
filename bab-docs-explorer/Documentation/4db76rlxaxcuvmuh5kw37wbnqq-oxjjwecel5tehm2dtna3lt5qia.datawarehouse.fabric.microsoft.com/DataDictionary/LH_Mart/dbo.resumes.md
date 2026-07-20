# dbo.resumes

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | varchar | 8000 | 1 |  |  |  |
| DateSaved | datetime2 | 8 | 1 |  |  |  |
| FirstName | varchar | 8000 | 1 |  |  |  |
| LastName | varchar | 8000 | 1 |  |  |  |
| WorkshopID | int | 4 | 1 |  |  |  |
| City | varchar | 8000 | 1 |  |  |  |
| State | varchar | 8000 | 1 |  |  |  |
| JobDepartment | varchar | 8000 | 1 |  |  |  |
| CareerType | varchar | 8000 | 1 |  |  |  |
| Position | varchar | 8000 | 1 |  |  |  |
| WillingToRelocate | bit | 1 | 1 |  |  |  |
| WillingToTravel | bit | 1 | 1 |  |  |  |
| Reference | varchar | 8000 | 1 |  |  |  |
| Resume | varchar | 8000 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
| UpdateDate | date | 3 | 1 |  |  |  |
