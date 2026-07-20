# dbo.loyaltytransactionfactstage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| LoyaltyTransactionType | varchar | 8000 | 1 |  |  |  |
| POSTransactionNumber | int | 4 | 1 |  |  |  |
| POSRegisterNumber | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| GaapUnits | decimal | 17 | 1 |  |  |  |
| matchedByEmail | int | 4 | 1 |  |  |  |
