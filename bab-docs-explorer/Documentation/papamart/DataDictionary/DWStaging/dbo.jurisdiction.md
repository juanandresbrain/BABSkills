# dbo.jurisdiction

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 0 |  |  |  |
| jurisdiction_description | nvarchar | 100 | 0 |  |  |  |
| jurisdiction_type | tinyint | 1 | 0 |  |  |  |
| tax_registration_number1 | nvarchar | 40 | 1 |  |  |  |
| tax_registration_number2 | nvarchar | 40 | 1 |  |  |  |
| country_id | decimal | 9 | 0 |  |  |  |
| pricing_rule_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_equivalency_rate | decimal | 5 | 1 |  |  |  |
| rate_last_modified | smalldatetime | 4 | 1 |  |  |  |
| home_jurisdiction_flag | bit | 1 | 0 |  |  |  |
| default_src_jurisdiction_flag | bit | 1 | 0 |  |  |  |
| availability_status | smallint | 2 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
