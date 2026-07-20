# dbo.mulesofttest_dynamicsdiscountline

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| DiscountCost | decimal | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | 8000 | 0 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 0 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| Percentage | int | 4 | 1 |  |  |  |
| RetailStoreId | varchar | 8000 | 1 |  |  |  |
| SaleLineNum | varchar | 8000 | 1 |  |  |  |
| CustomerDiscountType | varchar | 8000 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| ManualDiscountType | varchar | 8000 | 0 |  |  |  |
| PeriodicDiscountOfferId | varchar | 8000 | 1 |  |  |  |
| BabRetailDiscountTransUniqueLineNum | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | 8000 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1933249942 | bigint | 8 | 0 |  |  |  |
