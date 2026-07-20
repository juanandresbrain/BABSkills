# dbo.azure_transaction_detail_fact

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| TransactionID | varchar | 8000 | 1 |  |  |  |
| TransactionLineSeq | decimal | 9 | 1 |  |  |  |
| RegisterNumber | varchar | 8000 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionDateTime | datetime2 | 8 | 1 |  |  |  |
| StoreID | varchar | 8000 | 1 |  |  |  |
| UnitGrossAmount | decimal | 17 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| UnitDiscAmount | decimal | 17 | 1 |  |  |  |
| PartyFlag | varchar | 8000 | 1 |  |  |  |
| TransactionType | varchar | 8000 | 1 |  |  |  |
| LineObject | varchar | 8000 | 1 |  |  |  |
| TransactionNumber | varchar | 8000 | 1 |  |  |  |
| ReferenceNumber | varchar | 8000 | 1 |  |  |  |
| VatTaxAmount | decimal | 17 | 1 |  |  |  |
| UpsellDiscAllocated | decimal | 9 | 1 |  |  |  |
| ExtCost | decimal | 17 | 1 |  |  |  |
| LineAction | int | 4 | 1 |  |  |  |
| StoreKey | varchar | 8000 | 1 |  |  |  |
| TransactionKey | float | 8 | 1 |  |  |  |
