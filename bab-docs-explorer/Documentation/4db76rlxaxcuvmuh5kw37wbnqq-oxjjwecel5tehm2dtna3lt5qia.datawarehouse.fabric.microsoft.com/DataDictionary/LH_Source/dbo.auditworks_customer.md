# dbo.auditworks_customer

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| line_id | decimal | 5 | 1 |  |  |  |
| customer_role | int | 4 | 1 |  |  |  |
| more_info_flag | int | 4 | 1 |  |  |  |
| customer_sufficient | int | 4 | 1 |  |  |  |
| title | varchar | 8000 | 1 |  |  |  |
| first_name | varchar | 8000 | 1 |  |  |  |
| last_name | varchar | 8000 | 1 |  |  |  |
| address_1 | varchar | 8000 | 1 |  |  |  |
| address_2 | varchar | 8000 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| county | varchar | 8000 | 1 |  |  |  |
| state | varchar | 8000 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| post_code | varchar | 8000 | 1 |  |  |  |
| telephone_no1 | varchar | 8000 | 1 |  |  |  |
| telephone_no2 | varchar | 8000 | 1 |  |  |  |
| customer_no | decimal | 13 | 1 |  |  |  |
| pos_tax_jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| fax | varchar | 8000 | 1 |  |  |  |
| email_address | varchar | 8000 | 1 |  |  |  |
