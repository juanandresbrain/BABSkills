# dbo.wcaudit_exportvssalesdate

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| iStoreID | int | 4 | 1 |  |  |  |
| orders | int | 4 | 1 |  |  |  |
| AWSalesDate | datetime2 | 8 | 1 |  |  |  |
| ExportDate | datetime2 | 8 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| Amount_CC | decimal | 9 | 1 |  |  |  |
| Amount_GC | decimal | 9 | 1 |  |  |  |
| Amount_SFS | decimal | 9 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
