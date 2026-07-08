# dbo.commission_code_xref

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| lookup_category | nvarchar | 40 | 0 |  |  |  |
| lookup_type | nvarchar | 40 | 0 |  |  |  |
| lookup_value | numeric | 9 | 0 |  |  |  |
| commission_code | nvarchar | 40 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| lookup_alpha_value | nvarchar | 40 | 0 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| effective_to_date | datetime | 8 | 1 |  |  |  |
