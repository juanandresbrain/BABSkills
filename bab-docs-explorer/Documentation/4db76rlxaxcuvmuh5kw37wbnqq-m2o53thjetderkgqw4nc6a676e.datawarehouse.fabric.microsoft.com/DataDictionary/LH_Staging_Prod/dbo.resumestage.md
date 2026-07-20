# dbo.resumestage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
