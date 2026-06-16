# dbo.babw_amexUS

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SubmittingMerchant | varchar | 30 | 1 |  |  |  |
| SubmittingLocID | varchar | 30 | 1 |  |  |  |
| TranDate | varchar | 30 | 1 |  |  |  |
| AmexDate | varchar | 30 | 1 |  |  |  |
| SubmissionAmount | varchar | 30 | 1 |  |  |  |
| TransCount | varchar | 30 | 1 |  |  |  |
| TotalCharges | varchar | 30 | 1 |  |  |  |
| Credits | varchar | 30 | 1 |  |  |  |
| DiscountAmount | varchar | 30 | 1 |  |  |  |
| FeesIncentives | varchar | 30 | 1 |  |  |  |
| SettlementAmount | varchar | 30 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spAmex_Bank_Export](../../StoredProcedures/IntegrationStaging/dbo.spAmex_Bank_Export.md)

