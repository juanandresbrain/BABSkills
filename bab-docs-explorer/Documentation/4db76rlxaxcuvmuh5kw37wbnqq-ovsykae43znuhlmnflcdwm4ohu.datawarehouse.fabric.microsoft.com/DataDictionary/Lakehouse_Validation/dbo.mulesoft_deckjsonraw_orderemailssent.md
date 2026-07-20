# dbo.mulesoft_deckjsonraw_orderemailssent

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
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
| MSSQL_System_Uniquifier_1849773647 | bigint | 8 | 0 |  |  |  |
