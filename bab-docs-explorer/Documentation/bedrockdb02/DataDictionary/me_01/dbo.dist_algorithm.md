# dbo.dist_algorithm

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| algorithm_type | smallint | 2 | 0 | YES |  |  |
| name | nvarchar | 100 | 0 |  |  |  |
| algorithm_srlzd | nvarchar | -1 | 0 |  |  |  |
| result_srlzd | nvarchar | -1 | 0 |  |  |  |
| calculation_level_enum | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

