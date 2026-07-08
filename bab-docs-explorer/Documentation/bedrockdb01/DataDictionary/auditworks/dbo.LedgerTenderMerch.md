# dbo.LedgerTenderMerch

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_description | nvarchar | 510 | 0 |  |  |  |
| object_type_display_descr | nvarchar | 510 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| SumAmount | money | 8 | 1 |  |  |  |
