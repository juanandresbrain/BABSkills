# dbo.reportingvatdiscoveryfinal

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| FirstJumpMindDate | datetime2 | 8 | 1 |  |  |  |
| FirstDynamicsDate | date | 3 | 1 |  |  |  |
| SumVatTaxAmountDynamics | decimal | 17 | 1 |  |  |  |
| SumVatDataWarehouse | decimal | 17 | 1 |  |  |  |
| SumVatDataWarehouseDonation | decimal | 17 | 1 |  |  |  |
| DiffDWMinusDyn | decimal | 17 | 1 |  |  |  |
