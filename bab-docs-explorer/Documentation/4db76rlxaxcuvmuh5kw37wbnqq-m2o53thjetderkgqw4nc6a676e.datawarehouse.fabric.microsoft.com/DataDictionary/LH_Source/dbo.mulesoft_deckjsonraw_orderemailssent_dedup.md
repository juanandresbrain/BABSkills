# dbo.mulesoft_deckjsonraw_orderemailssent_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| OrderEmailSentID | bigint | 8 | 1 |  |  |  |
| TemplateName | varchar | 8000 | 1 |  |  |  |
| SentUTC | datetime2 | 8 | 1 |  |  |  |
| ToEmail | varchar | 8000 | 1 |  |  |  |
| ToName | varchar | 8000 | 1 |  |  |  |
| SentBy | varchar | 8000 | 1 |  |  |  |
| Success | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
