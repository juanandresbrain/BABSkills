# dbo.pick_review_parameter

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pick_review_parameter_id | int | 4 | 0 |  |  |  |
| merchandise_hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| warehouse_id | smallint | 2 | 0 |  |  |  |
| review_on_sunday | bit | 1 | 0 |  |  |  |
| review_on_monday | bit | 1 | 0 |  |  |  |
| review_on_tuesday | bit | 1 | 0 |  |  |  |
| review_on_wednesday | bit | 1 | 0 |  |  |  |
| review_on_thursday | bit | 1 | 0 |  |  |  |
| review_on_friday | bit | 1 | 0 |  |  |  |
| review_on_saturday | bit | 1 | 0 |  |  |  |
| cycle_frequency | smallint | 2 | 0 |  |  |  |
| last_execution | smalldatetime | 4 | 1 |  |  |  |
| force_pick_review_date | bit | 1 | 0 |  |  |  |
| distribution_description | nvarchar | 120 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| group_distribution_by | tinyint | 1 | 0 |  |  |  |
| cycle_period | tinyint | 1 | 0 |  |  |  |
| application_server_id | T_ID | 16 | 0 |  |  |  |
| next_execution | smalldatetime | 4 | 1 |  |  |  |
| next_pick_review_date | smalldatetime | 4 | 1 |  |  |  |
| min_constr_on_monday | int | 4 | 1 |  |  |  |
| min_constr_on_tuesday | int | 4 | 1 |  |  |  |
| min_constr_on_wednesday | int | 4 | 1 |  |  |  |
| min_constr_on_thursday | int | 4 | 1 |  |  |  |
| min_constr_on_friday | int | 4 | 1 |  |  |  |
| min_constr_on_saturday | int | 4 | 1 |  |  |  |
| min_constr_on_sunday | int | 4 | 1 |  |  |  |
| max_pack_type_per_loc | smallint | 2 | 0 |  |  |  |
| allow_pack_alloc_exceed_loc | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_unit | smallint | 2 | 0 |  |  |  |
| pack_size_threshold | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_pct | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingUpdatePickReviewParameters](../../StoredProcedures/me_01/dbo.spMerchandisingUpdatePickReviewParameters.md)
- [me_01: dbo.spMerchandisingWhsePickReviewSummary](../../StoredProcedures/me_01/dbo.spMerchandisingWhsePickReviewSummary.md)

