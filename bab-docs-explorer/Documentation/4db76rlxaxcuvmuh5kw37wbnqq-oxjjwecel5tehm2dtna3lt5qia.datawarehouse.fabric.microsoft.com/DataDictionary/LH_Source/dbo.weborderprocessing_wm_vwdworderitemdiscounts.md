# dbo.weborderprocessing_wm_vwdworderitemdiscounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| SKU | varchar | 8000 | 1 |  |  |  |
| ItemDiscountAmount | decimal | 17 | 1 |  |  |  |
| OrderDiscountAmount | decimal | 17 | 1 |  |  |  |
| TotalDiscountAmount | decimal | 17 | 1 |  |  |  |
| SourceSite | varchar | 8000 | 1 |  |  |  |
