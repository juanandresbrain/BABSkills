# dbo.imp_price_change

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_price_change_id | decimal | 9 | 0 | YES |  |  |
| price_change_duration | smallint | 2 | 0 |  |  |  |
| location_grouping | smallint | 2 | 0 |  |  |  |
| category_code | nvarchar | 40 | 0 |  |  |  |
| price_change_description | nvarchar | 120 | 1 |  |  |  |
| position_code | nvarchar | 40 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_to_date | smalldatetime | 4 | 1 |  |  |  |
| issue_date | smalldatetime | 4 | 1 |  |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| calculation_value | decimal | 9 | 1 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| pricing_rule_code | nvarchar | 40 | 1 |  |  |  |
| generate_tickets | smallint | 2 | 0 |  |  |  |
| print_by_location | nvarchar | 2 | 1 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| promotional_event | nvarchar | 2 | 1 |  |  |  |
| imp_file_name | nvarchar | 400 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_purge_$sp](../../StoredProcedures/me_01/dbo.import_pc_purge_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)

