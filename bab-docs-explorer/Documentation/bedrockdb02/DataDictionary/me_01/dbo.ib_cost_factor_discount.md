# dbo.ib_cost_factor_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_cost_factor_discount_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| extended_cost | decimal | 9 | 0 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| cost_factor_discount_id | smallint | 2 | 0 |  |  |  |
| extended_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.import_asn_third_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_third_step_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_cfd_$sp.md)
- [me_01: dbo.startup_ib_cost_factor_discount_$sp](../../StoredProcedures/me_01/dbo.startup_ib_cost_factor_discount_$sp.md)

