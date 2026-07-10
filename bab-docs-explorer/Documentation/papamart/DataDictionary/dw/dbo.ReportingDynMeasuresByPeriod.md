# dbo.ReportingDynMeasuresByPeriod

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RowKeyDyn | varchar | 30 | 0 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| MerchSalesDyn | numeric | 17 | 1 |  |  |  |
| MerchDiscountsDyn | numeric | 17 | 1 |  |  |  |
| GiftCardSales_Dyn | numeric | 17 | 0 |  |  |  |
| GiftCardDiscounts_Dyn | numeric | 17 | 0 |  |  |  |
| Donations_Dyn | numeric | 17 | 0 |  |  |  |
| DonationDiscounts_Dyn | numeric | 17 | 0 |  |  |  |
| SumTaxAmount_Dyn | numeric | 17 | 0 |  |  |  |
| SalesTotalDyn | numeric | 17 | 1 |  |  |  |
| AmericanExpress_Dyn | numeric | 9 | 0 |  |  |  |
| BABWGiftCardTender_Dyn | numeric | 9 | 0 |  |  |  |
| Cash_Dyn | numeric | 9 | 0 |  |  |  |
| Discover_Dyn | numeric | 9 | 0 |  |  |  |
| KlarnaRecievable_Dyn | numeric | 9 | 0 |  |  |  |
| MasterCard_Dyn | numeric | 9 | 0 |  |  |  |
| PayPalReceivable_Dyn | numeric | 9 | 0 |  |  |  |
| VisaTotals_Dyn | numeric | 9 | 0 |  |  |  |
| ADYENAMEX_Dyn | numeric | 9 | 0 |  |  |  |
| ADYENDISC_Dyn | numeric | 9 | 0 |  |  |  |
| ADYENMC_Dyn | numeric | 9 | 0 |  |  |  |
| ADYENPP_Dyn | numeric | 9 | 0 |  |  |  |
| ADYENVISA_Dyn | numeric | 9 | 0 |  |  |  |
| AMAZONREC_Dyn | numeric | 9 | 0 |  |  |  |
| Check_Dyn | numeric | 9 | 0 |  |  |  |
| DEBIT_Dyn | numeric | 9 | 0 |  |  |  |
| HOUSE_Dyn | numeric | 9 | 0 |  |  |  |
| JCB_Dyn | numeric | 9 | 0 |  |  |  |
| MAESTER_Dyn | numeric | 9 | 0 |  |  |  |
| PaperBearBucks_Dyn | numeric | 9 | 0 |  |  |  |
| PartyDepositVoucher_Dyn | numeric | 9 | 0 |  |  |  |
| WebStoreCredit_Dyn | numeric | 9 | 0 |  |  |  |
| PaymentTotalDyn | numeric | 17 | 1 |  |  |  |
