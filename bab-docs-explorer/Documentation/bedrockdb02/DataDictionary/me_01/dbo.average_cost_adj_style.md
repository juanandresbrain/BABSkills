# dbo.average_cost_adj_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| average_cost_adj_style_id | decimal | 9 | 0 | YES |  |  |
| average_cost_adjustment_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| use_level_flag | bit | 1 | 0 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| average_cost | decimal | 9 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| average_cost_local | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_avg_cost_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_avg_cost_adj_documents_$sp.md)

