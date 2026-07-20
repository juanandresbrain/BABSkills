# dbo.weborderdiscountsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| ItemDiscountAmount | decimal | 17 | 1 |  |  |  |
| OrderItemDiscountAmount | decimal | 17 | 1 |  |  |  |
| TotalDiscountAmount | decimal | 17 | 1 |  |  |  |
| SourceSite | varchar | 8000 | 1 |  |  |  |
