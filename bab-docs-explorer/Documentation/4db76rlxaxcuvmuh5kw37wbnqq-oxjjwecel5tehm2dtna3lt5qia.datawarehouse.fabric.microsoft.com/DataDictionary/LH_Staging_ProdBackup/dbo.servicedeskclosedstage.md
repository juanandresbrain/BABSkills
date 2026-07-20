# dbo.servicedeskclosedstage

**Database:** LH_Staging_ProdBackup  
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
| Source | varchar | 8000 | 1 |  |  |  |
| Team | varchar | 8000 | 1 |  |  |  |
| Area | varchar | 8000 | 1 |  |  |  |
| Category | varchar | 8000 | 1 |  |  |  |
| Subcategory | varchar | 8000 | 1 |  |  |  |
| ResolvedDateTime | datetime2 | 8 | 1 |  |  |  |
| Address1Country | varchar | 8000 | 1 |  |  |  |
| Problem_ID | varchar | 8000 | 1 |  |  |  |
| Avg_Days_Open | int | 4 | 1 |  |  |  |
| OpenWk | int | 4 | 1 |  |  |  |
| ClosedWk | int | 4 | 1 |  |  |  |
| OpenMon | int | 4 | 1 |  |  |  |
| CloseMo | int | 4 | 1 |  |  |  |
| OpenYr | int | 4 | 1 |  |  |  |
| CloseYr | int | 4 | 1 |  |  |  |
