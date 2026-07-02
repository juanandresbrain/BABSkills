# dbo.babw_adyen

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Company_Account | nvarchar | 100 | 1 |  |  |  |
| Merchant_Account | nvarchar | 100 | 1 |  |  |  |
| Store | nvarchar | 100 | 1 |  |  |  |
| Psp_Reference | nvarchar | 100 | 1 |  |  |  |
| Merchant_Reference | nvarchar | 510 | 1 |  |  |  |
| Payment_Method | nvarchar | 100 | 1 |  |  |  |
| Creation_Date | datetime2 | 8 | 1 |  |  |  |
| TimeZone | nvarchar | 100 | 1 |  |  |  |
| Type | nvarchar | 100 | 1 |  |  |  |
| Modification_Reference | nvarchar | 510 | 1 |  |  |  |
| Gross_Currency | nvarchar | 100 | 1 |  |  |  |
| Gross_Debit_GC | decimal | 9 | 1 |  |  |  |
| Gross_Credit_GC | decimal | 9 | 1 |  |  |  |
| Exchange_Rate | float | 8 | 1 |  |  |  |
| Net_Currency | nvarchar | 100 | 1 |  |  |  |
| Net_Debit_NC | decimal | 9 | 1 |  |  |  |
| Net_Credit_NC | decimal | 9 | 1 |  |  |  |
| Commission_NC | decimal | 9 | 1 |  |  |  |
| Markup_NC | decimal | 9 | 1 |  |  |  |
| Scheme_Fees_NC | decimal | 9 | 1 |  |  |  |
| Interchange_NC | decimal | 9 | 1 |  |  |  |
| Payment_Method_Variant | nvarchar | 100 | 1 |  |  |  |
| Modification_Merchant_Reference | nvarchar | 510 | 1 |  |  |  |
| Batch_Number | int | 4 | 1 |  |  |  |
| Reserved4 | nvarchar | 100 | 1 |  |  |  |
| Reserved5 | nvarchar | 100 | 1 |  |  |  |
| Reserved6 | nvarchar | 100 | 1 |  |  |  |
| Reserved7 | nvarchar | 100 | 1 |  |  |  |
| Reserved8 | nvarchar | 100 | 1 |  |  |  |
| Reserved9 | nvarchar | 100 | 1 |  |  |  |
| Reserved10 | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spAdyen_Bank_Export](../../StoredProcedures/IntegrationStaging/dbo.spAdyen_Bank_Export.md)

