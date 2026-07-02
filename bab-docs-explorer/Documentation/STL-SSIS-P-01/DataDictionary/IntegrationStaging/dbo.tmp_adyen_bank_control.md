# dbo.tmp_adyen_bank_control

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merchantAccount | varchar | 80 | 1 |  |  |  |
| CreatedDate | date | 3 | 1 |  |  |  |
| lastBatchNum | varchar | 5 | 1 |  |  |  |
| DayString | varchar | 10 | 1 |  |  |  |
| TimeString | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spAdyen_Bank_Export](../../StoredProcedures/IntegrationStaging/dbo.spAdyen_Bank_Export.md)

