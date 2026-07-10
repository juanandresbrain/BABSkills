# dbo.GiftCard_Destroy

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| Month | int | 4 | 1 |  |  |  |
| actual_date | smalldatetime | 4 | 1 |  |  |  |
| account_number | nvarchar | 510 | 1 |  |  |  |
| transaction_amount | float | 8 | 1 |  |  |  |
| userid | nvarchar | 510 | 1 |  |  |  |
| found | bit | 1 | 1 |  |  |  |
| current_value | money | 8 | 1 |  |  |  |
