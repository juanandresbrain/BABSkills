# dbo.DynamicsSalesDetailFacts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsSalesDetailFactsId | int | 4 | 0 | YES |  |  |
| CustAccount | varchar | 20 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
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
| PeriodicPercentageDiscount | numeric | 9 | 1 |  |  |  |
| TotalDiscAmount | numeric | 9 | 1 |  |  |  |
| TotalDiscPct | numeric | 9 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CurrentSentDate | datetime | 8 | 1 |  |  |  |
| NegativeSentDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
