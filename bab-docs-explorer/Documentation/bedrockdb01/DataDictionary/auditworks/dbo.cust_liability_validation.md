# dbo.cust_liability_validation

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| validation_id | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| default_priority_no | smallint | 2 | 0 |  |  |  |
| validation_description | nvarchar | 510 | 0 |  |  |  |
| reject_reason_description | nvarchar | 510 | 0 |  |  |  |
| liability_amount_factor | smallint | 2 | 0 |  |  |  |
| receivable_amount_factor | smallint | 2 | 0 |  |  |  |
| amount_3_factor | smallint | 2 | 0 |  |  |  |
| amount_4_factor | smallint | 2 | 0 |  |  |  |
| amount_5_factor | smallint | 2 | 0 |  |  |  |
| amount_6_factor | smallint | 2 | 0 |  |  |  |
| amount_7_factor | smallint | 2 | 0 |  |  |  |
| amount_8_factor | smallint | 2 | 0 |  |  |  |
| amount_9_factor | smallint | 2 | 0 |  |  |  |
| amount_10_factor | smallint | 2 | 0 |  |  |  |
| stocked_amount_factor | smallint | 2 | 0 |  |  |  |
| stocked_factor | smallint | 2 | 0 |  |  |  |
| stocked_stolen_factor | smallint | 2 | 0 |  |  |  |
| issued_factor | smallint | 2 | 0 |  |  |  |
| stolen_from_cust_factor | smallint | 2 | 0 |  |  |  |
| forfeited_factor | smallint | 2 | 0 |  |  |  |
| amount_outstanding_factor | smallint | 2 | 0 |  |  |  |
| units_outstanding_factor | smallint | 2 | 0 |  |  |  |
| units_2_factor | smallint | 2 | 0 |  |  |  |
| units_3_factor | smallint | 2 | 0 |  |  |  |
| units_4_factor | smallint | 2 | 0 |  |  |  |
| units_5_factor | smallint | 2 | 0 |  |  |  |
| entry_count_factor | smallint | 2 | 0 |  |  |  |
| include_current_amt | smallint | 2 | 0 |  |  |  |
| include_current_unit | smallint | 2 | 0 |  |  |  |
| sign_to_reject1 | smallint | 2 | 0 |  |  |  |
| sign_to_reject2 | smallint | 2 | 0 |  |  |  |
| applicability_code | smallint | 2 | 0 |  |  |  |
| validation_resource_id | numeric | 9 | 1 |  |  |  |
| reason_resource_id | numeric | 9 | 1 |  |  |  |
| display_control_reference_type | tinyint | 1 | 1 |  |  |  |
| subject_to_amount_change | tinyint | 1 | 0 |  |  |  |
