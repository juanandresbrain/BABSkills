# dbo.tmp_adyen_bank

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rowNum | int | 4 | 0 |  |  |  |
| rowNumNew | int | 4 | 1 |  |  |  |
| As Of | smalldatetime | 4 | 1 |  |  |  |
| Currency | varchar | 25 | 1 |  |  |  |
| BankID Type | varchar | 25 | 1 |  |  |  |
| BankID | varchar | 25 | 1 |  |  |  |
| Account | varchar | 25 | 1 |  |  |  |
| Data Type | varchar | 25 | 1 |  |  |  |
| BAI Code | varchar | 25 | 1 |  |  |  |
| Description | varchar | 25 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| Balance/Value Date | varchar | 25 | 1 |  |  |  |
| Customer Reference | varchar | 25 | 1 |  |  |  |
| Immediate Availability | varchar | 25 | 1 |  |  |  |
| 1 Day Float | varchar | 25 | 1 |  |  |  |
| 2+ DayFloat | varchar | 25 | 1 |  |  |  |
| Bank Reference | varchar | 25 | 1 |  |  |  |
| # of Items | varchar | 25 | 1 |  |  |  |
| Text | varchar | 25 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spAdyen_Bank_Export](../../StoredProcedures/IntegrationStaging/dbo.spAdyen_Bank_Export.md)

