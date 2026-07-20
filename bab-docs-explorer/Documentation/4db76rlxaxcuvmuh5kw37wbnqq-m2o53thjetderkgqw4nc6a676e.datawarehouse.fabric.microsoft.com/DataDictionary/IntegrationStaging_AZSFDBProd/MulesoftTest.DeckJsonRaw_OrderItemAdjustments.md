# MulesoftTest.DeckJsonRaw_OrderItemAdjustments

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| NetPrice | real | 4 | 1 |  |  |  |
| GrossPrice | real | 4 | 1 |  |  |  |
| PromotionID | varchar | -1 | 1 |  |  |  |
| CampaignID | varchar | -1 | 1 |  |  |  |
| DiscountText | varchar | -1 | 1 |  |  |  |
| CouponCode | varchar | -1 | 1 |  |  |  |
| AdjustmentType | bigint | 8 | 1 |  |  |  |
| AdjustmentTypeValue | varchar | -1 | 1 |  |  |  |
| AdjustmentClassificationID | bigint | 8 | 1 |  |  |  |
| OrderTransactionIdentifier | bigint | 8 | 1 |  |  |  |
| AdjustmentClassificationText | varchar | -1 | 1 |  |  |  |
| AdjustmentDate | datetime2 | 8 | 1 |  |  |  |
| OrderItemID | bigint | 8 | 1 |  |  |  |
| AdjustmentMultiplier | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1833773590 | bigint | 8 | 0 |  |  |  |
