# dbo.bank_deposit_source

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deposit_source | smallint | 2 | 0 |  |  |  |
| deposit_category | smallint | 2 | 0 |  |  |  |
| source_description | nvarchar | 510 | 0 |  |  |  |
| source_line_object | smallint | 2 | 0 |  |  |  |
| acceptable_short | money | 8 | 0 |  |  |  |
| assume_deposit | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_mon | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_tue | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_wed | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_thu | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_fri | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_sat | tinyint | 1 | 0 |  |  |  |
| deposit_lag_days_sun | tinyint | 1 | 0 |  |  |  |
| interface_id | tinyint | 1 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
