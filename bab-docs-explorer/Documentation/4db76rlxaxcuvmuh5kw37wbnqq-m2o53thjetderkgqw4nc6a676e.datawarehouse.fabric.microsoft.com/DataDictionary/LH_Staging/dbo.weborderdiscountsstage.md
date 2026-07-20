# dbo.weborderdiscountsstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
