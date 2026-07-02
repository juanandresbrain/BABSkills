# dbo.item_5404

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |
| SKU | nvarchar | 40 | 0 |  |  |  |
| ItemID | bigint | 8 | 1 |  |  |  |
| Div | bigint | 8 | 1 |  |  |  |
| ItemName | nvarchar | 60 | 1 |  |  |  |
| ItemDesc | nvarchar | 100 | 1 |  |  |  |
| Dept | decimal | 5 | 1 |  |  |  |
| SubDept | bigint | 8 | 1 |  |  |  |
| Cat | decimal | 5 | 1 |  |  |  |
| SubCat | bigint | 8 | 1 |  |  |  |
| SizeCode | nvarchar | 20 | 1 |  |  |  |
| SizeType | nvarchar | 8 | 1 |  |  |  |
| ColorCode | nvarchar | 12 | 1 |  |  |  |
| StyleCode | nvarchar | 40 | 1 |  |  |  |
| LifeStyleCode | nvarchar | 8 | 1 |  |  |  |
| Brand | nvarchar | 60 | 1 |  |  |  |
| Season | nvarchar | 8 | 1 |  |  |  |
| PermPrice | decimal | 9 | 1 |  |  |  |
| MfgSugPrice | decimal | 9 | 1 |  |  |  |
| POSDesc | nvarchar | 50 | 1 |  |  |  |
| DiscountCode | int | 4 | 1 |  |  |  |
| CustDiscountCode | int | 4 | 1 |  |  |  |
| EmplDiscountCode | int | 4 | 1 |  |  |  |
| ThreshDiscountCode | int | 4 | 1 |  |  |  |
| MarkdownCode | int | 4 | 1 |  |  |  |
| PriceOverrideCode | int | 4 | 1 |  |  |  |
| AlertCode | nvarchar | 40 | 1 |  |  |  |
| Class | decimal | 5 | 1 |  |  |  |
| SubClass | decimal | 5 | 1 |  |  |  |
| FiscalYear | bigint | 8 | 1 |  |  |  |
| MeasUnitCode | nvarchar | 8 | 1 |  |  |  |
| WtUnitCode | nvarchar | 8 | 1 |  |  |  |
| PkgWt | decimal | 9 | 1 |  |  |  |
| CustOrderFlg | int | 4 | 1 |  |  |  |
| DirectOrderFlg | int | 4 | 1 |  |  |  |
| ItemKeyWord | nvarchar | 50 | 1 |  |  |  |
| TaxGroup | decimal | 5 | 1 |  |  |  |
| AcctRestrictId | bigint | 8 | 1 |  |  |  |
| AccntLimitFlg | int | 4 | 1 |  |  |  |
| AgeRestrictCode | nvarchar | 20 | 1 |  |  |  |
| SpecialRestrictCode | nvarchar | 20 | 1 |  |  |  |
| AllowQtyKeyFlg | int | 4 | 1 |  |  |  |
| PriceEntryFlg | int | 4 | 1 |  |  |  |
| SerialNoFlg | int | 4 | 1 |  |  |  |
| OpenDrawerFlg | int | 4 | 1 |  |  |  |
| SpiffCode | nvarchar | 20 | 1 |  |  |  |
| BusDiscountCode | int | 4 | 1 |  |  |  |
| AllowRetFlg | int | 4 | 1 |  |  |  |
| CouponMltplFlg | int | 4 | 1 |  |  |  |
| PriceVerifyFlg | int | 4 | 1 |  |  |  |
| WeightEntryFlg | int | 4 | 1 |  |  |  |
| CustLoyaltyFlg | int | 4 | 1 |  |  |  |
| CustLoyaltyCnt | int | 4 | 1 |  |  |  |
| CouponFlg | int | 4 | 1 |  |  |  |
| FoodStampFlg | int | 4 | 1 |  |  |  |
| GiveAwayFlg | int | 4 | 1 |  |  |  |
| PromotionFlg | int | 4 | 1 |  |  |  |
| Cost | decimal | 9 | 1 |  |  |  |
| UnitPriceFactor | decimal | 5 | 1 |  |  |  |
| LongItemDesc | nvarchar | 510 | 1 |  |  |  |
| ImageName | nvarchar | 510 | 1 |  |  |  |
| ItemStatusCode | nvarchar | 8 | 1 |  |  |  |
| AlertType | nvarchar | 8 | 1 |  |  |  |
| AssociationGrpId | bigint | 8 | 1 |  |  |  |
| Modelnum | nvarchar | 100 | 1 |  |  |  |
| PriceAuthAmt | decimal | 9 | 1 |  |  |  |
| ActivateFlg | int | 4 | 1 |  |  |  |
| TenderTypeId | int | 4 | 1 |  |  |  |
| ItemTypeCode | nvarchar | 8 | 1 |  |  |  |
| BuyBackPrice | decimal | 9 | 1 |  |  |  |
| DefectItemActionCode | nvarchar | 8 | 1 |  |  |  |
| CustOrderMinAmount | decimal | 9 | 1 |  |  |  |
| AvailableDate | datetime | 8 | 1 |  |  |  |
| HostItemNum | nvarchar | 40 | 1 |  |  |  |

