# dbo.tmpAllocationsAdjWMS

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | bigint | 8 | 1 |  |  |  |
| distribution_line | float | 8 | 1 |  |  |  |
| UPC | nvarchar | 24 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| Adj_qty | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spOutputWMSAllocAdj](../../StoredProcedures/IntegrationStaging/WMS.spOutputWMSAllocAdj.md)

