# dbo.mulesoft_deckjsonraw_orderadjustments

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| AdjustmentType | bigint | 8 | 1 |  |  |  |
| AdjustmentTypeValue | varchar | 8000 | 1 |  |  |  |
| NetPrice | real | 4 | 1 |  |  |  |
| GrossPrice | real | 4 | 1 |  |  |  |
| PromotionID | varchar | 8000 | 1 |  |  |  |
| CampaignID | varchar | 8000 | 1 |  |  |  |
| DiscountText | varchar | 8000 | 1 |  |  |  |
| CouponCode | varchar | 8000 | 1 |  |  |  |
| AdjustmentClassificationID | bigint | 8 | 1 |  |  |  |
| AdjustmentClassificationText | varchar | 8000 | 1 |  |  |  |
| AdjustmentDate | datetime2 | 8 | 1 |  |  |  |
| OrderTransactionIdentifier | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1865773704 | bigint | 8 | 0 |  |  |  |
