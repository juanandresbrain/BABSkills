# dbo.usp_AW_to_CUBE_validation_email_aw_data

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | datetime | 8 | 0 |  |  |  |
| transaction_id_AW | numeric | 9 | 0 |  |  |  |
| voucher_adjustment | numeric | 17 | 1 |  |  |  |
| GAAPSales_AW | numeric | 17 | 1 |  |  |  |
