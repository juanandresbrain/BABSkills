# dbo.TflBatch

**Database:** SurveyResults  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TflBatchId | int | 4 | 0 |  |  |  |
| ProcessName | nvarchar | 200 | 0 |  |  |  |
| EntityName | nvarchar | 200 | 0 |  |  |  |
| BinaryVersion | binary | 8 | 1 |  |  |  |
| StringVersion | nvarchar | 128 | 1 |  |  |  |
| DateTimeVersion | datetime | 8 | 1 |  |  |  |
| Int64Version | bigint | 8 | 1 |  |  |  |
| Int32Version | int | 4 | 1 |  |  |  |
| Int16Version | smallint | 2 | 1 |  |  |  |
| ByteVersion | tinyint | 1 | 1 |  |  |  |
| TflUpdate | datetime | 8 | 0 |  |  |  |
| Inserts | bigint | 8 | 0 |  |  |  |
| Updates | bigint | 8 | 0 |  |  |  |
| Deletes | bigint | 8 | 0 |  |  |  |
