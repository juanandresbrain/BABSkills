# dbo.experianfootfall_tmpspexport_salespos_holdonedayonly

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
| TransactionCount | int | 4 | 1 |  |  |  |
| UnitsSold | int | 4 | 1 |  |  |  |
| SalesValue | decimal | 17 | 1 |  |  |  |
| NumberOfRefunds | int | 4 | 1 |  |  |  |
| RefundValue | decimal | 9 | 1 |  |  |  |
