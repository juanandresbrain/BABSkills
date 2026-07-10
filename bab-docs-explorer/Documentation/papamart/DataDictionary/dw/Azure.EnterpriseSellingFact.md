# Azure.EnterpriseSellingFact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | decimal | 9 | 0 |  |  |  |
| LineSeq | decimal | 5 | 1 |  |  |  |
| StoreNumber | varchar | 10 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| ReferenceNumber | varchar | 80 | 1 |  |  |  |
| HasNonESitems | varchar | 3 | 0 |  |  |  |
| ESAction | nvarchar | 510 | 1 |  |  |  |
| ProductKey | int | 4 | 0 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| UnitGrossAmount | decimal | 5 | 0 |  |  |  |
| UnitNetAmount | decimal | 5 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 5 | 0 |  |  |  |
