# dbo.comp_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comp_set_id | bigint | 8 | 0 | YES |  |  |
| comp_set_name | nvarchar | 40 | 0 |  |  |  |
| comp_set_description | nvarchar | 120 | 1 |  |  |  |
| picking_priority | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

