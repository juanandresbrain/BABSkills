# dbo.azure_wh_inventory

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| OnHand | decimal | 9 | 1 |  |  |  |
| workYear | varchar | 8000 | 1 |  |  |  |
| WorkWeek | varchar | 8000 | 1 |  |  |  |
| WHType | varchar | 8000 | 1 |  |  |  |
| DateKey | datetime2 | 8 | 1 |  |  |  |
| FiscalWeekKey | datetime2 | 8 | 1 |  |  |  |
| Ohio980 Available | bigint | 8 | 1 |  |  |  |
| OhioLocked Available | bigint | 8 | 1 |  |  |  |
| Other Available | bigint | 8 | 1 |  |  |  |
| UK2970 Available | bigint | 8 | 1 |  |  |  |
| WC960 Available | bigint | 8 | 1 |  |  |  |
| WH Allocated | bigint | 8 | 1 |  |  |  |
| WH Damaged | bigint | 8 | 1 |  |  |  |
| WH Discrepancy | bigint | 8 | 1 |  |  |  |
| WH In Transit | bigint | 8 | 1 |  |  |  |
| WH Pending Shrink | bigint | 8 | 1 |  |  |  |
| WH Reserved Cust Order | bigint | 8 | 1 |  |  |  |
