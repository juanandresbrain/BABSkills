# dbo.count_import_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| zone_label | nvarchar | 30 | 1 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| date_imported | smalldatetime | 4 | 0 |  |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| total_retail | decimal | 9 | 1 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| total_valuation_retail | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.pi_process_loc_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_$sp.md)

