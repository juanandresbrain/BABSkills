# dbo.experianfootfall_tmpspexport_staffinglabor_output

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CompanyID | int | 4 | 1 |  |  |  |
| HierarchyID | int | 4 | 1 |  |  |  |
| NodeName | varchar | 8000 | 1 |  |  |  |
| CGValueType | int | 4 | 1 |  |  |  |
| TimeGrain | int | 4 | 1 |  |  |  |
| SiteIdentity | int | 4 | 1 |  |  |  |
| DateAndTime | datetime2 | 8 | 1 |  |  |  |
| MinutesWorked | int | 4 | 1 |  |  |  |
| HoursWorkedCalculation | decimal | 9 | 1 |  |  |  |
| NumberOfStaffForExport | varchar | 8000 | 1 |  |  |  |
| HoursWorkedForExport | varchar | 8000 | 1 |  |  |  |
| StaffCosts | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
