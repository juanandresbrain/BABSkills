# dbo.OLE DB Destination

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductNumber | varchar | 6 | 1 |  |  |  |
| InventoryUnitSymbol | nvarchar | 8000 | 1 |  |  |  |
| FromUnitSymbol | nvarchar | 8000 | 1 |  |  |  |
| ToUnitSymbol | nvarchar | 8000 | 1 |  |  |  |
| Factor | float | 8 | 1 |  |  |  |
| WeightKG | float | 8 | 1 |  |  |  |
| ProductDescription | varchar | 30 | 1 |  |  |  |
| UnitCost | numeric | 17 | 1 |  |  |  |

