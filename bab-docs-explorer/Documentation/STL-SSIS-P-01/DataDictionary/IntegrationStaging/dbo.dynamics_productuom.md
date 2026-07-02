# dbo.dynamics_productuom

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductNumber | nvarchar | 50 | 1 |  |  |  |
| Denominator | int | 4 | 1 |  |  |  |
| Factor | numeric | 17 | 1 |  |  |  |
| fromSymbol | nvarchar | 20 | 1 |  |  |  |
| InnerOffset | numeric | 17 | 1 |  |  |  |
| toSymbol | nvarchar | 20 | 1 |  |  |  |
| Numerator | int | 4 | 1 |  |  |  |
| OuterOffset | numeric | 17 | 1 |  |  |  |

