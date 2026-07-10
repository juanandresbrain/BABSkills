# dbo.tmpEml

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_id | int | 4 | 1 |  |  |  |
| Emailable | int | 4 | 1 |  |  |  |
| email_opt_in_date | datetime | 8 | 1 |  |  |  |
| email_address | nvarchar | 130 | 1 |  |  |  |
| email_indicator | tinyint | 1 | 1 |  |  |  |
| email_opt_in_flag | tinyint | 1 | 1 |  |  |  |
| create_store_no | int | 4 | 1 |  |  |  |
