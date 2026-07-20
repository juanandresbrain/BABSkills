# dbo.weborderdiscountssatge

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | datetime2 | 8 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| ItemDiscountAmount | decimal | 17 | 1 |  |  |  |
| OrderItemDiscountAmount | decimal | 17 | 1 |  |  |  |
| TotalDiscountAmount | decimal | 17 | 1 |  |  |  |
| SourceSite | varchar | 8000 | 1 |  |  |  |
