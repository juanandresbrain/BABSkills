# dbo.oo_all_styleclr_chn_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |
| on_order_retail_te | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [ma_01: dbo.hk_style_delete_oo_all_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_oo_all_$sp.md)
- [ma_01: dbo.post_oo_all_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_styleclr_$sp.md)
- [ma_01: dbo.post_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_oo_style_color_$sp.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)

