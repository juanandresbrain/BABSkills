# dbo.azure_service_desk_open

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Incident | int | 4 | 1 |  |  |  |
| Summary | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| Priority | varchar | 8000 | 1 |  |  |  |
| Customer | varchar | 8000 | 1 |  |  |  |
| CustomerLocation | varchar | 8000 | 1 |  |  |  |
| Owner | varchar | 8000 | 1 |  |  |  |
| Created_On | datetime2 | 8 | 1 |  |  |  |
| CreateDate | date | 3 | 1 |  |  |  |
| Source | varchar | 8000 | 1 |  |  |  |
| Team | varchar | 8000 | 1 |  |  |  |
| Area | varchar | 8000 | 1 |  |  |  |
| Category | varchar | 8000 | 1 |  |  |  |
| Subcategory | varchar | 8000 | 1 |  |  |  |
| ResolvedDateTime | datetime2 | 8 | 1 |  |  |  |
| ResolvedDate | date | 3 | 1 |  |  |  |
| Description | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| Owner_Email | varchar | 8000 | 1 |  |  |  |
| Problem | varchar | 8000 | 1 |  |  |  |
| OpenWK | int | 4 | 1 |  |  |  |
| OpenMo | int | 4 | 1 |  |  |  |
| OpenYr | int | 4 | 1 |  |  |  |
