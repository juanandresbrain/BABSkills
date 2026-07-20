# dbo.stagingexchangerate

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
