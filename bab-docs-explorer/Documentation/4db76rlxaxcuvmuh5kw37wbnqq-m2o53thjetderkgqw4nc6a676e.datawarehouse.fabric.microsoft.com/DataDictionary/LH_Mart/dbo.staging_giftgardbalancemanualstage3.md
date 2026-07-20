# dbo.staging_giftgardbalancemanualstage3

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CardNumber | varchar | 8000 | 1 |  |  |  |
| RemainingBalance | varchar | 8000 | 1 |  |  |  |
| ActivationDate | varchar | 8000 | 1 |  |  |  |
| LastReloadDate | varchar | 8000 | 1 |  |  |  |
| TotalReloadAmount | varchar | 8000 | 1 |  |  |  |
| LastTransactionDate | varchar | 8000 | 1 |  |  |  |
| LastFinancialTransactionDate | varchar | 8000 | 1 |  |  |  |
| LastPositiveTransactionDate | varchar | 8000 | 1 |  |  |  |
| ActivationMerchantNumber | varchar | 8000 | 1 |  |  |  |
| ActivationAltMerchantNumber | varchar | 8000 | 1 |  |  |  |
| StateOfActivation | varchar | 8000 | 1 |  |  |  |
| PromoNumber | varchar | 8000 | 1 |  |  |  |
| PromoDescription | varchar | 8000 | 1 |  |  |  |
| hasCardNumber | int | 4 | 1 |  |  |  |
| StagedFileName | varchar | 8000 | 1 |  |  |  |
| ActivationDateDerived | varchar | 8000 | 1 |  |  |  |
| ActivationDateDerivedSource | varchar | 8000 | 1 |  |  |  |
