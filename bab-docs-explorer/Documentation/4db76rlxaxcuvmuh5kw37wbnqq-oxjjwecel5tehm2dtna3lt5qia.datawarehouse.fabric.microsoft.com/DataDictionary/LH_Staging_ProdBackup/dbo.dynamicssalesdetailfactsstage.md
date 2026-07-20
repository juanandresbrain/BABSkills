# dbo.dynamicssalesdetailfactsstage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustAccount | varchar | 8000 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| TransactionLineSeq | decimal | 5 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| OriginalPrice | decimal | 9 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| ItemId | varchar | 8000 | 1 |  |  |  |
| LineDscAmount | decimal | 9 | 1 |  |  |  |
| DiscAmount | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 8000 | 1 |  |  |  |
| VatTaxAmount | decimal | 9 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| LineObject | int | 4 | 1 |  |  |  |
| LineAction | int | 4 | 1 |  |  |  |
| BlankSoundChipItemId | varchar | 8000 | 1 |  |  |  |
