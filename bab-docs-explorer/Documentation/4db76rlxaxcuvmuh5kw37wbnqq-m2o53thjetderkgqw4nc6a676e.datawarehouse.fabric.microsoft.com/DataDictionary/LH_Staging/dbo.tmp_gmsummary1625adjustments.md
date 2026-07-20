# dbo.tmp_gmsummary1625adjustments

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_period | int | 4 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 8000 | 1 |  |  |  |
| isGCCoupon | int | 4 | 1 |  |  |  |
| numRecs | int | 4 | 1 |  |  |  |
| discAmount | decimal | 17 | 1 |  |  |  |
| minDate | datetime2 | 8 | 1 |  |  |  |
| maxDate | datetime2 | 8 | 1 |  |  |  |
