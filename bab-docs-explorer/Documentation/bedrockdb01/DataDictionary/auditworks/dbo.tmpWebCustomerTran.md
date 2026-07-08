# dbo.tmpWebCustomerTran

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| email_address | nvarchar | 100 | 1 |  |  |  |
| first_name | nvarchar | 40 | 1 |  |  |  |
| last_name | nvarchar | 80 | 1 |  |  |  |
| address_1 | nvarchar | 80 | 1 |  |  |  |
| address_2 | nvarchar | 80 | 1 |  |  |  |
| city | nvarchar | 80 | 1 |  |  |  |
| state | nvarchar | 80 | 1 |  |  |  |
| post_code | nvarchar | 40 | 1 |  |  |  |
| country | varchar | 3 | 0 |  |  |  |
| telephone_no1 | nvarchar | 32 | 1 |  |  |  |
| PhoneTxtOptIn | int | 4 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
