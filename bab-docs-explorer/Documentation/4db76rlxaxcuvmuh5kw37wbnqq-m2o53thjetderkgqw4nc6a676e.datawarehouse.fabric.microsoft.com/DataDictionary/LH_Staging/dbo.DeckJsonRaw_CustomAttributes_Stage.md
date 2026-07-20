# dbo.DeckJsonRaw_CustomAttributes_Stage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| Name | varchar | 8000 | 1 |  |  |  |
| Value | varchar | 8000 | 1 |  |  |  |
| IsUxVisible | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
