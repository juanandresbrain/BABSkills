# dbo.azure_pchealthchecks

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Hostname | varchar | 8000 | 1 |  |  |  |
| Store | varchar | 8000 | 1 |  |  |  |
| Role | varchar | 8000 | 1 |  |  |  |
| Model | varchar | 8000 | 1 |  |  |  |
| GoPostReportErrors | int | 4 | 1 |  |  |  |
| GoPostReportWarnings | int | 4 | 1 |  |  |  |
| Description | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| DateTime | datetime2 | 8 | 1 |  |  |  |
| Date | date | 3 | 1 |  |  |  |
