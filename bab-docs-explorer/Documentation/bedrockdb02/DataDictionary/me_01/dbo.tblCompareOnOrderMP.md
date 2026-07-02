# dbo.tblCompareOnOrderMP

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| on_order_units | int | 4 | 1 |  |  |  |
| merch_period | tinyint | 1 | 0 |  |  |  |
| merch_year | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)

