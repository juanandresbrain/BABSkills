# MulesoftTest.DynamicsDiscountLineOms

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | -1 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| DiscountCost | decimal | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | -1 | 0 |  |  |  |
| RetailTerminalId | varchar | -1 | 1 |  |  |  |
| RetailTransactionId | varchar | -1 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | -1 | 0 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| Percentage | int | 4 | 1 |  |  |  |
| RetailStoreId | varchar | -1 | 1 |  |  |  |
| SaleLineNum | varchar | -1 | 1 |  |  |  |
| CustomerDiscountType | varchar | -1 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| ManualDiscountType | varchar | -1 | 0 |  |  |  |
| PeriodicDiscountOfferId | varchar | -1 | 1 |  |  |  |
| BabRetailDiscountTransUniqueLineNum | bigint | 8 | 1 |  |  |  |
| Entity | varchar | -1 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | -1 | 1 |  |  |  |
| InventLocationId | varchar | -1 | 1 |  |  |  |
| BatchID | varchar | -1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1510296440 | bigint | 8 | 0 |  |  |  |
