# dbo.TempTenderDate

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| SumAmount | money | 8 | 1 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_description | nvarchar | 510 | 0 |  |  |  |
| Line_object_type_desc | nvarchar | 510 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
