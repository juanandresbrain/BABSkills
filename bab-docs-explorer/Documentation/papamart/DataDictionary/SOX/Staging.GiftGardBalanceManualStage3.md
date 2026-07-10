# Staging.GiftGardBalanceManualStage3

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CardNumber | varchar | 50 | 1 |  |  |  |
| RemainingBalance | varchar | 50 | 1 |  |  |  |
| ActivationDate | varchar | 50 | 1 |  |  |  |
| LastReloadDate | varchar | 50 | 1 |  |  |  |
| TotalReloadAmount | varchar | 50 | 1 |  |  |  |
| LastTransactionDate | varchar | 50 | 1 |  |  |  |
| LastFinancialTransactionDate | varchar | 50 | 1 |  |  |  |
| LastPositiveTransactionDate | varchar | 50 | 1 |  |  |  |
| ActivationMerchantNumber | varchar | 50 | 1 |  |  |  |
| ActivationAltMerchantNumber | varchar | 50 | 1 |  |  |  |
| StateOfActivation | varchar | 50 | 1 |  |  |  |
| PromoNumber | varchar | 50 | 1 |  |  |  |
| PromoDescription | varchar | 50 | 1 |  |  |  |
| hasCardNumber | int | 4 | 1 |  |  |  |
| StagedFileName | varchar | 400 | 1 |  |  |  |
| ActivationDateDerived | varchar | 50 | 1 |  |  |  |
| ActivationDateDerivedSource | varchar | 50 | 1 |  |  |  |
