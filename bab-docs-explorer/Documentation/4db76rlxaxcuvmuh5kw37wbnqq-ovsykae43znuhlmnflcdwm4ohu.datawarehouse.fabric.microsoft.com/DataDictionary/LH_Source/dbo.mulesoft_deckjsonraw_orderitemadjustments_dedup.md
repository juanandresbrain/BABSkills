# dbo.mulesoft_deckjsonraw_orderitemadjustments_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| NetPrice | real | 4 | 1 |  |  |  |
| GrossPrice | real | 4 | 1 |  |  |  |
| PromotionID | varchar | 8000 | 1 |  |  |  |
| CampaignID | varchar | 8000 | 1 |  |  |  |
| DiscountText | varchar | 8000 | 1 |  |  |  |
| CouponCode | varchar | 8000 | 1 |  |  |  |
| AdjustmentType | bigint | 8 | 1 |  |  |  |
| AdjustmentTypeValue | varchar | 8000 | 1 |  |  |  |
| AdjustmentClassificationID | bigint | 8 | 1 |  |  |  |
| OrderTransactionIdentifier | bigint | 8 | 1 |  |  |  |
| AdjustmentClassificationText | varchar | 8000 | 1 |  |  |  |
| AdjustmentDate | datetime2 | 8 | 1 |  |  |  |
| OrderItemID | bigint | 8 | 1 |  |  |  |
| AdjustmentMultiplier | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
