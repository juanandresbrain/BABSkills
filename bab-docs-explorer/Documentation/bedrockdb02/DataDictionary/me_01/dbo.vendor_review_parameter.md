# dbo.vendor_review_parameter

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_review_parameter_id | int | 4 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| merchandise_hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| cycle_frequency | smallint | 2 | 0 |  |  |  |
| last_execution | smalldatetime | 4 | 1 |  |  |  |
| generate_po | bit | 1 | 0 |  |  |  |
| retain_for_distribution | bit | 1 | 0 |  |  |  |
| group_distribution_by | tinyint | 1 | 0 |  |  |  |
| distribution_description | nvarchar | 120 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| expected_receipt_date_days | smallint | 2 | 0 |  |  |  |
| review_on_sunday | bit | 1 | 0 |  |  |  |
| review_on_monday | bit | 1 | 0 |  |  |  |
| review_on_tuesday | bit | 1 | 0 |  |  |  |
| review_on_wednesday | bit | 1 | 0 |  |  |  |
| review_on_thursday | bit | 1 | 0 |  |  |  |
| review_on_friday | bit | 1 | 0 |  |  |  |
| review_on_saturday | bit | 1 | 0 |  |  |  |
| cycle_period | tinyint | 1 | 0 |  |  |  |
| application_server_id | T_ID | 16 | 0 |  |  |  |
| next_execution | smalldatetime | 4 | 1 |  |  |  |
| schedule_no | int | 4 | 1 |  |  |  |
| max_pack_type_per_loc | smallint | 2 | 0 |  |  |  |
| allow_pack_alloc_exceed_loc | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_unit | smallint | 2 | 0 |  |  |  |
| pack_size_threshold | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_pct | smallint | 2 | 0 |  |  |  |
| submit_generated_po | bit | 1 | 0 |  |  |  |

