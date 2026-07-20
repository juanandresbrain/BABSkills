# dbo.jumpmind_sls_order_package

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| package_type_id | varchar | 8000 | 1 |  |  |  |
| package_type_display_name | varchar | 8000 | 1 |  |  |  |
| carrier_id | varchar | 8000 | 1 |  |  |  |
| carrier_display_name | varchar | 8000 | 1 |  |  |  |
| tracking_number | varchar | 8000 | 1 |  |  |  |
| shipping_label | varbinary | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| tracking_url | varchar | 8000 | 1 |  |  |  |
| label_data | varchar | 8000 | 1 |  |  |  |
| package_weight | varchar | 8000 | 1 |  |  |  |
| weight_u_o_m | varchar | 8000 | 1 |  |  |  |
| package_length | varchar | 8000 | 1 |  |  |  |
| package_width | varchar | 8000 | 1 |  |  |  |
| package_height | varchar | 8000 | 1 |  |  |  |
| dimensions_u_o_m | varchar | 8000 | 1 |  |  |  |
