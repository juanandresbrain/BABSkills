# MulesoftTest.DynamicsSalesLineOms

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | -1 | 1 |  |  |  |
| CustAccount | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | -1 | 1 |  |  |  |
| LineNum | varchar | -1 | 1 |  |  |  |
| OriginalPrice | float | 8 | 1 |  |  |  |
| Price | float | 8 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | -1 | 1 |  |  |  |
| RetailTransactionid | varchar | -1 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | -1 | 0 |  |  |  |
| RetailTerminalId | varchar | -1 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| ItemId | varchar | -1 | 1 |  |  |  |
| LineDscAmount | decimal | 9 | 1 |  |  |  |
| DiscAmount | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | -1 | 1 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | -1 | 1 |  |  |  |
| PeriodicPercentageDiscount | float | 8 | 1 |  |  |  |
| TotalDiscamount | decimal | 9 | 1 |  |  |  |
| TotalDiscPct | float | 8 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | -1 | 1 |  |  |  |
| ShippingDescription | varchar | -1 | 1 |  |  |  |
| LineItemType | varchar | -1 | 1 |  |  |  |
| NativeItemId | varchar | -1 | 1 |  |  |  |
| BatchID | varchar | -1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| BearId | varchar | -1 | 1 |  |  |  |
| ExtShipmentNumber | varchar | -1 | 1 |  |  |  |
| DeliveryMode | varchar | -1 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1638296896 | bigint | 8 | 0 |  |  |  |
