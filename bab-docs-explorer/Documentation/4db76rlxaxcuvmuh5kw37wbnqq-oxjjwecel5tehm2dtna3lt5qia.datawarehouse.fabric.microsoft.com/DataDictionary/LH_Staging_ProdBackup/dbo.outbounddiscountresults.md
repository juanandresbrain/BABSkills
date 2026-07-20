# dbo.outbounddiscountresults

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| dmDiscountID | int | 4 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
| isExpired | bit | 1 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| unit_Gross_Amount | decimal | 9 | 1 |  |  |  |
| numRedeemed | int | 4 | 1 |  |  |  |
