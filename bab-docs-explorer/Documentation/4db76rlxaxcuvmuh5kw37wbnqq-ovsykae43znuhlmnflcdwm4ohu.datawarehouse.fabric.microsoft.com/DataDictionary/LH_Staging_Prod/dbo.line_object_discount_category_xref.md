# dbo.line_object_discount_category_xref

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Line_Object | int | 4 | 1 |  |  |  |
| categoryType | varchar | 8000 | 1 |  |  |  |
| channelType | varchar | 8000 | 1 |  |  |  |
| needsReview | bit | 1 | 1 |  |  |  |
