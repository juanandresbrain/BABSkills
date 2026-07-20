# dbo.flashsalessummary

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| BusinessHour | int | 4 | 1 |  |  |  |
| TYGaapByHourNative | decimal | 17 | 1 |  |  |  |
| TYGaapByHourUSD | decimal | 17 | 1 |  |  |  |
| TYGaapByHourRunningTotalNative | decimal | 17 | 1 |  |  |  |
| TYGaapByHourRunningTotalUSD | decimal | 17 | 1 |  |  |  |
| TYTransCountByHour | int | 4 | 1 |  |  |  |
| TYTransCountRunningTotal | int | 4 | 1 |  |  |  |
| TYNetUnitsByHour | int | 4 | 1 |  |  |  |
| TYNetUnitsRunningTotal | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
