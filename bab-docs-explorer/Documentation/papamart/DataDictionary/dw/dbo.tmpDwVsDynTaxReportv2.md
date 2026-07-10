# dbo.tmpDwVsDynTaxReportv2

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionSourceSystem | varchar | 4 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| Dw_transaction_id | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 5 | 1 |  |  |  |
| Register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| Enterprise_Selling_Amount | numeric | 17 | 1 |  |  |  |
| DwGrossSales | numeric | 17 | 1 |  |  |  |
| DwDiscounts | numeric | 17 | 1 |  |  |  |
| DwSubtotal | numeric | 9 | 1 |  |  |  |
| DwTaxAmount | numeric | 9 | 1 |  |  |  |
| DwTotalDue | numeric | 9 | 1 |  |  |  |
| JumpMindTaxExtract | numeric | 9 | 1 |  |  |  |
| AmexDw | numeric | 9 | 1 |  |  |  |
| VISA\MC\DISCOVER_Dw | numeric | 9 | 1 |  |  |  |
| CashDw | numeric | 9 | 0 |  |  |  |
| BABWGiftCardTenderDw | numeric | 9 | 1 |  |  |  |
| OtherTenderTypeDw | numeric | 13 | 1 |  |  |  |
| DynGrossSales | numeric | 17 | 0 |  |  |  |
| DynDiscounts | numeric | 17 | 0 |  |  |  |
| DynSubtotal | numeric | 9 | 1 |  |  |  |
| DynTaxAmount | numeric | 17 | 0 |  |  |  |
| DynTotalDue | numeric | 17 | 1 |  |  |  |
| AmexDyn | numeric | 9 | 1 |  |  |  |
| VISA\MC\DISCOVER_Dyn | numeric | 9 | 1 |  |  |  |
| CashDyn | numeric | 9 | 0 |  |  |  |
| BABWGiftCardTenderDyn | numeric | 9 | 0 |  |  |  |
| OtherTenderTypeDyn | numeric | 13 | 1 |  |  |  |
| TaxDiff | numeric | 17 | 1 |  |  |  |
