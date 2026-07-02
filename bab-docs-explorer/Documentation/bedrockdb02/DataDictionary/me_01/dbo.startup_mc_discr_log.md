# dbo.startup_mc_discr_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_mc_discr_log_id | int | 4 | 0 |  |  |  |
| proc_name | nvarchar | 200 | 0 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| third_key_id | smallint | 2 | 1 |  |  |  |
| document_no | nvarchar | 40 | 1 |  |  |  |
| end_time | datetime | 8 | 0 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_discrepancy_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_cfd_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_inv_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_inv_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_oo_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_oo_$sp.md)

