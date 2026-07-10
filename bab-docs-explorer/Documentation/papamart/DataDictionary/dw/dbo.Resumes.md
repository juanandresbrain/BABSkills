# dbo.Resumes

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | uniqueidentifier | 16 | 1 |  |  |  |
| DateSaved | datetime | 8 | 1 |  |  |  |
| FirstName | varchar | 150 | 1 |  |  |  |
| LastName | varchar | 150 | 1 |  |  |  |
| WorkshopID | int | 4 | 1 |  |  |  |
| City | varchar | 255 | 1 |  |  |  |
| State | varchar | 50 | 1 |  |  |  |
| JobDepartment | varchar | 150 | 1 |  |  |  |
| CareerType | varchar | 75 | 1 |  |  |  |
| Position | varchar | 255 | 1 |  |  |  |
| WillingToRelocate | bit | 1 | 1 |  |  |  |
| WillingToTravel | bit | 1 | 1 |  |  |  |
| Reference | varchar | 100 | 1 |  |  |  |
| Resume | ntext | 16 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
| UpdateDate | date | 3 | 1 |  |  |  |
