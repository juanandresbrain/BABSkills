# dbo.stagingexchangerate

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ConversionFactor | varchar | 8000 | 1 |  |  |  |
| EndDate | datetime2 | 8 | 1 |  |  |  |
| FromCurrency | varchar | 8000 | 1 |  |  |  |
| Rate | decimal | 9 | 1 |  |  |  |
| RateTypeDescription | varchar | 8000 | 1 |  |  |  |
| RateTypeName | varchar | 8000 | 1 |  |  |  |
| StartDate | datetime2 | 8 | 1 |  |  |  |
| ToCurrency | varchar | 8000 | 1 |  |  |  |
