# dbo.avg_cost_adj_style_loc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| avg_cost_adj_style_loc_id | decimal | 9 | 0 | YES |  |  |
| average_cost_adj_style_id | decimal | 9 | 0 |  |  |  |
| average_cost_adjustment_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_avg_cost_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_avg_cost_adj_documents_$sp.md)

