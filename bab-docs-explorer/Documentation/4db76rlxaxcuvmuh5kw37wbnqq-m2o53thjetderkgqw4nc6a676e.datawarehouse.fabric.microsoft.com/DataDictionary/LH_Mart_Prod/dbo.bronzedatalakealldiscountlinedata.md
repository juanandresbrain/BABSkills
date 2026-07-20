# dbo.bronzedatalakealldiscountlinedata

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionDate | date | 3 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| DiscountCost | decimal | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | 8000 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| LineNum | int | 4 | 1 |  |  |  |
| RetailStoreId | varchar | 8000 | 1 |  |  |  |
| SaleLineNum | int | 4 | 1 |  |  |  |
| PeriodicDiscountOfferId | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
