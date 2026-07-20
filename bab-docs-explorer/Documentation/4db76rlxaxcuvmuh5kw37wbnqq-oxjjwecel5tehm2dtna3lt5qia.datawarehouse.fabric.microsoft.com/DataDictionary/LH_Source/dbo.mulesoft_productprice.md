# dbo.mulesoft_productprice

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseID | varchar | 40 | 1 |  |  |  |
| StyleCode | varchar | 40 | 1 |  |  |  |
| Jurisdiction | varchar | 40 | 1 |  |  |  |
| AVAILB | varchar | 40 | 1 |  |  |  |
| OriginalRetailDecimal | decimal | 9 | 1 |  |  |  |
| CurrentRetailDecimal | decimal | 9 | 1 |  |  |  |
| OriginalRetail1200Decimal | decimal | 9 | 1 |  |  |  |
| isCurrent | int | 4 | 1 |  |  |  |
| StartDate | datetime2 | 8 | 1 |  |  |  |
| StopDate | datetime2 | 8 | 1 |  |  |  |
| ChangeType | varchar | 40 | 1 |  |  |  |
| CreateDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Source | varchar | 200 | 1 |  |  |  |
