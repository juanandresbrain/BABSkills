# dbo.OutboundDiscountResults

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| dmDiscountID | int | 4 | 0 |  |  |  |
| categoryTypeID | int | 4 | 0 |  |  |  |
| isExpired | bit | 1 | 0 |  |  |  |
| transaction_id | decimal | 9 | 0 |  |  |  |
| country | varchar | 50 | 1 |  |  |  |
| unit_Gross_Amount | money | 8 | 1 |  |  |  |
| numRedeemed | int | 4 | 1 |  |  |  |
