# dbo.report_tracing

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| trace_source | nvarchar | 100 | 0 |  |  |  |
| trace_object | nvarchar | 1000 | 0 |  |  |  |
| trace_timestamp | datetime | 8 | 1 |  |  |  |
| trace_value | nvarchar | -1 | 1 |  |  |  |
| trace_comment | nvarchar | -1 | 1 |  |  |  |
