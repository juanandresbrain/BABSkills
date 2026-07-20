# dbo.emailrevenuesummary

**Database:** LH_Temp  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RID | int | 4 | 1 |  |  |  |
| SendDate | date | 3 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| retRev | decimal | 17 | 1 |  |  |  |
| webRev | decimal | 17 | 1 |  |  |  |
