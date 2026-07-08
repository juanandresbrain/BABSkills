# dbo.tax_rate

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_until_date | smalldatetime | 4 | 1 |  |  |  |
| tax_rate_code_description | nvarchar | 510 | 1 |  |  |  |
| combined_rate | numeric | 5 | 0 |  |  |  |
| federal_rate | numeric | 5 | 0 |  |  |  |
| state_rate | numeric | 5 | 0 |  |  |  |
| county_rate | numeric | 5 | 0 |  |  |  |
| city_rate | numeric | 5 | 0 |  |  |  |
| district_rate | numeric | 5 | 0 |  |  |  |
| threshold_amount | smallmoney | 4 | 0 |  |  |  |
| tax_on_threshold_excess | tinyint | 1 | 0 |  |  |  |
| tax_on_tax_level | tinyint | 1 | 0 |  |  |  |
| below_threshold_combined_rate | numeric | 5 | 1 |  |  |  |
| below_federal_rate | numeric | 5 | 1 |  |  |  |
| below_state_rate | numeric | 5 | 1 |  |  |  |
| below_county_rate | numeric | 5 | 1 |  |  |  |
| below_city_rate | numeric | 5 | 1 |  |  |  |
| below_district_rate | numeric | 5 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| item_tax_strip_flag | tinyint | 1 | 1 |  |  |  |
| tax_rate_id | numeric | 9 | 1 |  |  |  |
| tax_schedule_id | binary | 16 | 1 |  |  |  |
| transaction_level_tax_calc | tinyint | 1 | 1 |  |  |  |
| compound_order | int | 4 | 0 |  |  |  |
| exemption_tax_rate_code | tinyint | 1 | 1 |  |  |  |
