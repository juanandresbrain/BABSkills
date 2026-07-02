# dbo.posting_parameter_20_JUN_2016

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 |  |  |  |
| posting_date | smalldatetime | 4 | 0 |  |  |  |
| starting_job_id | int | 4 | 0 |  |  |  |
| from_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| to_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| from_ib_cost_factor_disc_id | decimal | 9 | 1 |  |  |  |
| to_ib_cost_factor_disc_id | decimal | 9 | 1 |  |  |  |
| from_ib_allocation_id | decimal | 9 | 1 |  |  |  |
| to_ib_allocation_id | decimal | 9 | 1 |  |  |  |
| from_ib_on_order_id | decimal | 9 | 1 |  |  |  |
| to_ib_on_order_id | decimal | 9 | 1 |  |  |  |
| init_posting_flag | bit | 1 | 0 |  |  |  |
| cmp_posting_flag | bit | 1 | 0 |  |  |  |
| flsh_posting_flag | bit | 1 | 0 |  |  |  |
| hist_posting_flag | bit | 1 | 0 |  |  |  |
| oh_posting_flag | bit | 1 | 0 |  |  |  |
| oo_all_posting_flag | bit | 1 | 0 |  |  |  |
| cmp_first_phase_flag | bit | 1 | 0 |  |  |  |
| flsh_first_phase_flag | bit | 1 | 0 |  |  |  |
| hist_first_phase_flag | bit | 1 | 0 |  |  |  |
| oh_first_phase_flag | bit | 1 | 0 |  |  |  |
| oo_all_first_phase_flag | bit | 1 | 0 |  |  |  |

