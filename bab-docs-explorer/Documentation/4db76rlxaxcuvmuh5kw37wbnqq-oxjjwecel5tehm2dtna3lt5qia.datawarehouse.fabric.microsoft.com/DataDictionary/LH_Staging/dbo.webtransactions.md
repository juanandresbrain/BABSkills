# dbo.webtransactions

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| TransactionNum | varchar | 8000 | 1 |  |  |  |
| TransactionDateTime | datetime2 | 8 | 1 |  |  |  |
| TaxAmount | decimal | 9 | 1 |  |  |  |
| TaxJurisdiction | varchar | 8000 | 1 |  |  |  |
