# dbo.DynamicsSalesLineStage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 136 | 1 |  |  |  |
| CustAccount | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 50 | 1 |  |  |  |
| LineNum | varchar | 50 | 1 |  |  |  |
| OriginalPrice | numeric | 9 | 1 |  |  |  |
| Price | numeric | 9 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| RetailReceiptId | varchar | 50 | 1 |  |  |  |
| RetailTransactionid | varchar | 138 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 14 | 0 |  |  |  |
| RetailTerminalId | varchar | 53 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| ItemId | varchar | 50 | 1 |  |  |  |
| LineDscAmount | numeric | 9 | 1 |  |  |  |
| DiscAmount | numeric | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 50 | 1 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| PeriodicPercentageDiscount | numeric | 13 | 1 |  |  |  |
| TotalDiscamount | numeric | 9 | 1 |  |  |  |
| TotalDiscPct | numeric | 17 | 1 |  |  |  |
| CreateTime | datetime | 8 | 1 |  |  |  |
| Barcode | varchar | 50 | 1 |  |  |  |
| ShippingDescription | varchar | 100 | 1 |  |  |  |
| LineItemType | varchar | 50 | 1 |  |  |  |
| NativeItemId | varchar | 100 | 1 |  |  |  |
| BearId | varchar | 25 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics3_BuildSalesLineStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics3_BuildSalesLineStagingTable.md)
- [WebOrderProcessing: dbo.spBabDynamics6_BlankSoundChipInsert](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics6_BlankSoundChipInsert.md)
- [WebOrderProcessing: dbo.spBabDynamics7_ShippingLineInserts](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics7_ShippingLineInserts.md)

