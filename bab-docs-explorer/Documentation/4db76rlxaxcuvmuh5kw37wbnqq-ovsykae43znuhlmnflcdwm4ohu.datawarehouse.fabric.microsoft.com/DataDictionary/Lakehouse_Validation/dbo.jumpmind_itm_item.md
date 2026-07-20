# dbo.jumpmind_itm_item

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| item_id | varchar | 8000 | 1 |  |  |  |
| item_name | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| long_description | varchar | 8000 | 1 |  |  |  |
| tax_group_id | varchar | 8000 | 1 |  |  |  |
| tax_exempt_code | int | 4 | 1 |  |  |  |
| type_code | varchar | 8000 | 1 |  |  |  |
| tare_weight | decimal | 17 | 1 |  |  |  |
| family_code | varchar | 8000 | 1 |  |  |  |
| expiration_date | datetime2 | 8 | 1 |  |  |  |
| product_id | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| stuffable | int | 4 | 1 |  |  |  |
| item_copy_id | varchar | 8000 | 1 |  |  |  |
