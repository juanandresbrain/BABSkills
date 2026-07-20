# dbo.jurisdiction

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_id | int | 4 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| jurisdiction_description | varchar | 8000 | 1 |  |  |  |
| jurisdiction_type | int | 4 | 1 |  |  |  |
| tax_registration_number1 | varchar | 8000 | 1 |  |  |  |
| tax_registration_number2 | varchar | 8000 | 1 |  |  |  |
| country_id | decimal | 9 | 1 |  |  |  |
| pricing_rule_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_equivalency_rate | decimal | 5 | 1 |  |  |  |
| rate_last_modified | datetime2 | 8 | 1 |  |  |  |
| home_jurisdiction_flag | bit | 1 | 1 |  |  |  |
| default_src_jurisdiction_flag | bit | 1 | 1 |  |  |  |
| availability_status | int | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
