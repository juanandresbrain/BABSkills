# dbo.enum_resource

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| enum | nvarchar | 20 | 0 | YES |  |  |
| resource_name | nvarchar | 510 | 0 |  |  |  |
| enum_type | nvarchar | 60 | 0 | YES |  |  |
| sort_sequence | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_lookup_enum_$sp](../../StoredProcedures/me_01/dbo.get_lookup_enum_$sp.md)
- [me_01: dbo.get_lookup_enum_int_$sp](../../StoredProcedures/me_01/dbo.get_lookup_enum_int_$sp.md)

