# dbo.inventory_status

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_status_id | smallint | 2 | 1 |  |  |  |
| inventory_status_code | varchar | 8000 | 1 |  |  |  |
| inventory_status_desc | varchar | 8000 | 1 |  |  |  |
| include_on_hand_totals_flag | bit | 1 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
