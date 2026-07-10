# dbo.ReportingVatDiscoveryFinal

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventLocationId | varchar | 4 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| FirstJumpMindDate | smalldatetime | 4 | 1 |  |  |  |
| FirstDynamicsDate | date | 3 | 1 |  |  |  |
| SumVatTaxAmountDynamics | numeric | 17 | 1 |  |  |  |
| SumVatDataWarehouse | decimal | 17 | 1 |  |  |  |
| SumVatDataWarehouseDonation | decimal | 17 | 1 |  |  |  |
| DiffDWMinusDyn | numeric | 17 | 1 |  |  |  |
