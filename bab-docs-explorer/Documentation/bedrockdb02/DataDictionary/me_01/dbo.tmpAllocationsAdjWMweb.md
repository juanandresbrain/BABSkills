# dbo.tmpAllocationsAdjWMweb

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_no | varchar | 14 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| distribution_number | nvarchar | 40 | 0 |  |  |  |
| allocated_units | int | 4 | 0 |  |  |  |
| sent_units | numeric | 17 | 1 |  |  |  |
| adj_qty | int | 4 | 1 |  |  |  |
| dist_line_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWMAllocAdjWEB](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWMAllocAdjWEB.md)

