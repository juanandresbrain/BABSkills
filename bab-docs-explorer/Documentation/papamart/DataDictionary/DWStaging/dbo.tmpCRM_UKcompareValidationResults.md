# dbo.tmpCRM_UKcompareValidationResults

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| email_address | nvarchar | 130 | 1 |  |  |  |
| customer_no | numeric | 13 | 0 |  |  |  |
| email_indicator | tinyint | 1 | 1 |  |  |  |
| email_opt_in_flag | tinyint | 1 | 1 |  |  |  |
| attribute_grouping_code | nchar | 8 | 1 |  |  |  |
| attribute_code | nchar | 10 | 1 |  |  |  |
| attribute_value | real | 4 | 1 |  |  |  |
| inDE | tinyint | 1 | 1 |  |  |  |
