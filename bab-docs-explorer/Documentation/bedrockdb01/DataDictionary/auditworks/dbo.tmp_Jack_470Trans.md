# dbo.tmp_Jack_470Trans

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| customer_info_exists | tinyint | 1 | 0 |  |  |  |
| first_Name | varchar | 20 | 1 |  |  |  |
| last_Name | varchar | 40 | 1 |  |  |  |
| customer_no | numeric | 13 | 1 |  |  |  |
