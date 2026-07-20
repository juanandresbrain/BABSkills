# dbo.crmtranfactprerollstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| LifetimeTransactionCount | int | 4 | 1 |  |  |  |
| LifetimeRecencyCount | int | 4 | 1 |  |  |  |
| LifetimeSalesTotal | decimal | 17 | 1 |  |  |  |
| FirstTransactionDate | date | 3 | 1 |  |  |  |
| LastTransDate | date | 3 | 1 |  |  |  |
| FirstStoreConcept | varchar | 8000 | 1 |  |  |  |
| LastTransStore | varchar | 8000 | 1 |  |  |  |
