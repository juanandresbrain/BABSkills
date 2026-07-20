# dbo.mulesoft_deckjsonraw_extended_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| Key | varchar | 8000 | 1 |  |  |  |
| Value | varchar | 8000 | 1 |  |  |  |
| Additional | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| OrderId | bigint | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
