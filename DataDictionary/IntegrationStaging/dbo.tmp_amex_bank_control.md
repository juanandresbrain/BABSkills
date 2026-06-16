# dbo.tmp_amex_bank_control

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CreatedDate | date | 3 | 1 |  |  |  |
| lastBatchNum | varchar | 5 | 1 |  |  |  |
| DayString | varchar | 10 | 1 |  |  |  |
| TimeString | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spAmex_Bank_Export](../../StoredProcedures/IntegrationStaging/dbo.spAmex_Bank_Export.md)

