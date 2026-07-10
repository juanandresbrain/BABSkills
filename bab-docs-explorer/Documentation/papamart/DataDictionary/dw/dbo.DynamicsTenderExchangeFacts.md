# dbo.DynamicsTenderExchangeFacts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
| line_sequence | numeric | 5 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| line_object_description | nvarchar | 510 | 1 |  |  |  |
| line_action_display_descr | nvarchar | 510 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| gross_line_amount | numeric | 9 | 1 |  |  |  |
| pos_discount_amount | numeric | 9 | 1 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| tender_key | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
