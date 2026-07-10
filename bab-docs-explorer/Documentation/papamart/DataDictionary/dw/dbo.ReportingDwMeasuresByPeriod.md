# dbo.ReportingDwMeasuresByPeriod

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RowKey | varchar | 31 | 0 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 5 | 1 |  |  |  |
| MerchSalesDW | numeric | 17 | 1 |  |  |  |
| MerchDiscountsDW | numeric | 17 | 1 |  |  |  |
| GiftCardSalesDW | numeric | 17 | 0 |  |  |  |
| GiftCardDiscountsDW | numeric | 17 | 0 |  |  |  |
| DonationsDW | numeric | 17 | 0 |  |  |  |
| DonationDiscountsDW | numeric | 17 | 0 |  |  |  |
| SumTaxAmountDW | numeric | 17 | 0 |  |  |  |
| SalesTotalDw | numeric | 17 | 1 |  |  |  |
| AmericanExpressDw | numeric | 9 | 0 |  |  |  |
| BABWGiftCardTenderDw | numeric | 9 | 0 |  |  |  |
| CashDw | numeric | 9 | 0 |  |  |  |
| DiscoverDw | numeric | 9 | 0 |  |  |  |
| KlarnaRecievableDw | numeric | 9 | 0 |  |  |  |
| MasterCardDw | numeric | 9 | 0 |  |  |  |
| PayPalReceivableDw | numeric | 9 | 0 |  |  |  |
| VisaTotalsDw | numeric | 9 | 0 |  |  |  |
| AdyenAmexDW | numeric | 9 | 0 |  |  |  |
| AdyenDiscoverDw | numeric | 9 | 0 |  |  |  |
| AdyenMastercardDw | numeric | 9 | 0 |  |  |  |
| AdyenPayPalDw | numeric | 9 | 0 |  |  |  |
| AdyenVisaDw | numeric | 9 | 0 |  |  |  |
| AmazonReceivableDw | numeric | 9 | 0 |  |  |  |
| BABChargeAccountDw | numeric | 9 | 0 |  |  |  |
| CheckDw | numeric | 9 | 0 |  |  |  |
| DebitCardDw | numeric | 9 | 0 |  |  |  |
| GlobalEReceivableDw | numeric | 9 | 0 |  |  |  |
| HouseChargeDw | numeric | 9 | 0 |  |  |  |
| JCB_Dw | numeric | 9 | 0 |  |  |  |
| MAESTR_Dw | numeric | 9 | 0 |  |  |  |
| PaperBearBucksDw | numeric | 9 | 0 |  |  |  |
| PartyDepositVoucherStr#337Dw | numeric | 9 | 0 |  |  |  |
| SerializedCouponDw | numeric | 9 | 0 |  |  |  |
| WebStoreCreditDw | numeric | 9 | 0 |  |  |  |
| PaymentTotalDW | numeric | 17 | 1 |  |  |  |
