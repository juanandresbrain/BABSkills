# dbo.mulesoft_productprice_stage

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseID | varchar | 8000 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| availb | varchar | 8000 | 1 |  |  |  |
| OriginalRetailDecimal | decimal | 9 | 1 |  |  |  |
| CurrentRetailDecimal | decimal | 9 | 1 |  |  |  |
| TrackingDate | datetime2 | 8 | 1 |  |  |  |
| isCurrent | bit | 1 | 1 |  |  |  |
| StartDate | datetime2 | 8 | 1 |  |  |  |
| StopDate | datetime2 | 8 | 1 |  |  |  |
| old_original_retail | decimal | 9 | 1 |  |  |  |
| old_current_retail | decimal | 9 | 1 |  |  |  |
| already_exists | int | 4 | 1 |  |  |  |
| Diff | int | 4 | 1 |  |  |  |
| ChangeType | varchar | 8000 | 1 |  |  |  |
