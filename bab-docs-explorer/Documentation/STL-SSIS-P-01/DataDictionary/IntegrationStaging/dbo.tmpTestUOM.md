# dbo.tmpTestUOM

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RECID | bigint | 8 | 1 |  |  |  |
| Denominator | int | 4 | 1 |  |  |  |
| Factor | numeric | 9 | 1 |  |  |  |
| FromUnitOfMeasure | bigint | 8 | 1 |  |  |  |
| Product | bigint | 8 | 1 |  |  |  |
| ToUnitOfMeasure | bigint | 8 | 1 |  |  |  |
| DataLakeModified_DateTime | datetime2 | 8 | 1 |  |  |  |

