# dbo.JMC_sls_transBACKUP

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| business_date | smalldatetime | 4 | 1 |  |  |  |
| business_unit_id | varchar | 128 | 1 |  |  |  |
| device_id | varchar | 128 | 1 |  |  |  |
| trans_type | varchar | 128 | 1 |  |  |  |
| trans_status | varchar | 128 | 1 |  |  |  |
| total | numeric | 9 | 1 |  |  |  |
| subtotal | numeric | 9 | 1 |  |  |  |
| tax_total | numeric | 9 | 1 |  |  |  |
| discount_total | numeric | 9 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| loyalty_card_number | varchar | 128 | 1 |  |  |  |
| customer_id | varchar | 128 | 1 |  |  |  |
| trans_nbr | bigint | 8 | 1 |  |  |  |
| username | varchar | 128 | 1 |  |  |  |
| create_time | datetime | 8 | 1 |  |  |  |
| last_update_time | datetime | 8 | 1 |  |  |  |
