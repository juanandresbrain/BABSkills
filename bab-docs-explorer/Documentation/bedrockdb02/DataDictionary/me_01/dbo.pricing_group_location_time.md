# dbo.pricing_group_location_time

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pricing_group_location_id | decimal | 9 | 0 | YES |  |  |
| pricing_group_id | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| begin_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.build_pg_time_table_$sp](../../StoredProcedures/me_01/dbo.build_pg_time_table_$sp.md)
- [me_01: dbo.plu_get_location_info_$sp](../../StoredProcedures/me_01/dbo.plu_get_location_info_$sp.md)
- [me_01: dbo.pop_25nov25_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.pop_25nov25_temp_sale_master_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)

