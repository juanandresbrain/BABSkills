# dbo.GiftCard_DeadCards

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| actual_date | smalldatetime | 4 | 1 |  |  |  |
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| account_number | nvarchar | 510 | 1 |  |  |  |
| request_code | float | 8 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| internal_request_code | float | 8 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| balance | money | 8 | 1 |  |  |  |
| Activation Store | nvarchar | 510 | 1 |  |  |  |
| found | bit | 1 | 1 |  |  |  |
| current_value | money | 8 | 1 |  |  |  |
