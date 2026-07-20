# dbo.azure_merchonorder

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_ID | decimal | 9 | 1 |  |  |  |
| Location_id | int | 4 | 1 |  |  |  |
| Fiscal_Year | varchar | 8000 | 1 |  |  |  |
| Fiscal_Period | varchar | 8000 | 1 |  |  |  |
| On_Order | int | 4 | 1 |  |  |  |
| DateKey | datetime2 | 8 | 1 |  |  |  |
| PeriodKey | int | 4 | 1 |  |  |  |
| TotalFlag | int | 4 | 1 |  |  |  |
