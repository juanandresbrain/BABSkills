# dbo.azure_enterprisesellingfact

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | decimal | 9 | 1 |  |  |  |
| LineSeq | decimal | 5 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| TransactionDate | datetime2 | 8 | 1 |  |  |  |
| ReferenceNumber | varchar | 8000 | 1 |  |  |  |
| HasNonESitems | varchar | 8000 | 1 |  |  |  |
| ESAction | varchar | 8000 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| UnitGrossAmount | decimal | 5 | 1 |  |  |  |
| UnitNetAmount | decimal | 5 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 5 | 1 |  |  |  |
