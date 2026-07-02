# dbo.imp_price_change_resubmit

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| ready_to_resubmit | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_$sp.md)
- [me_01: dbo.import_pc_batch_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_$sp.md)

