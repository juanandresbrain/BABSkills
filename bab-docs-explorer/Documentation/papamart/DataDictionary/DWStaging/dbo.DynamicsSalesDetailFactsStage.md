# dbo.DynamicsSalesDetailFactsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustAccount | varchar | 20 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| TransactionLineSeq | decimal | 5 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| OriginalPrice | numeric | 9 | 1 |  |  |  |
| Price | numeric | 9 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8 | 1 |  |  |  |
| RetailTerminalId | varchar | 10 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| ItemId | varchar | 50 | 1 |  |  |  |
| LineDscAmount | numeric | 9 | 1 |  |  |  |
| DiscAmount | numeric | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 80 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 10 | 1 |  |  |  |
| VatTaxAmount | numeric | 9 | 1 |  |  |  |
| CurrencyCode | varchar | 3 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
| LineObject | int | 4 | 1 |  |  |  |
| LineAction | int | 4 | 1 |  |  |  |
| BlankSoundChipItemId | varchar | 30 | 1 |  |  |  |
