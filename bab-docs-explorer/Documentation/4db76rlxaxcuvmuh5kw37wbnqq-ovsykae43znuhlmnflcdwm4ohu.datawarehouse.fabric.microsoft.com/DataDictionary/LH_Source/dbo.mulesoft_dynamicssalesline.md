# dbo.mulesoft_dynamicssalesline

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| CustAccount | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| LineNum | varchar | 8000 | 1 |  |  |  |
| OriginalPrice | float | 8 | 1 |  |  |  |
| Price | float | 8 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionid | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 0 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| ItemId | varchar | 8000 | 1 |  |  |  |
| LineDscAmount | decimal | 9 | 1 |  |  |  |
| DiscAmount | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| PeriodicPercentageDiscount | float | 8 | 1 |  |  |  |
| TotalDiscamount | decimal | 9 | 1 |  |  |  |
| TotalDiscPct | float | 8 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | 8000 | 1 |  |  |  |
| ShippingDescription | varchar | 8000 | 1 |  |  |  |
| LineItemType | varchar | 8000 | 1 |  |  |  |
| NativeItemId | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| BearId | varchar | 8000 | 1 |  |  |  |
| ExtShipmentNumber | varchar | 8000 | 1 |  |  |  |
| DeliveryMode | varchar | 8000 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1965250056 | bigint | 8 | 0 |  |  |  |
