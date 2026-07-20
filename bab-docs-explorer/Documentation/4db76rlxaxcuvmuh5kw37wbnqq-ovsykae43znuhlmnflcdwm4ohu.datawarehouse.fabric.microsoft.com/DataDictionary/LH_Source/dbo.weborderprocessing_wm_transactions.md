# dbo.weborderprocessing_wm_transactions

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| TransactionNum | varchar | 8000 | 1 |  |  |  |
| ClientID | varchar | 8000 | 1 |  |  |  |
| TransactionDateTime | datetime2 | 8 | 1 |  |  |  |
| TaxAmount | decimal | 9 | 1 |  |  |  |
| TaxJurisdiction | varchar | 8000 | 1 |  |  |  |
| TaxAuthority | varchar | 8000 | 1 |  |  |  |
| TaxType | int | 4 | 1 |  |  |  |
| tmpTransID | int | 4 | 1 |  |  |  |
