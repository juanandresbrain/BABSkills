# dbo.merchsales_view_stage_padded

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| FiscalYear | varchar | 8000 | 1 |  |  |  |
| FiscalWeek | varchar | 8000 | 1 |  |  |  |
| NetSalesUnits | decimal | 9 | 1 |  |  |  |
| NetSalesRetail | decimal | 17 | 1 |  |  |  |
| DateKey | datetime2 | 8 | 1 |  |  |  |
