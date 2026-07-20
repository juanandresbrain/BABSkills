# dbo.dynamicssalesdetailfacts

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsSalesDetailFactsId | int | 4 | 1 |  |  |  |
| CustAccount | varchar | 8000 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
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
| PeriodicPercentageDiscount | decimal | 9 | 1 |  |  |  |
| TotalDiscAmount | decimal | 9 | 1 |  |  |  |
| TotalDiscPct | decimal | 9 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| CurrentSentDate | datetime2 | 8 | 1 |  |  |  |
| NegativeSentDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
