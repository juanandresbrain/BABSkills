# dbo.imp_jur_tax_exception

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_jur_tax_exception_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 0 |  |  |  |
| tax_type_code | nvarchar | 10 | 0 |  |  |  |
| tax_rate_code | nvarchar | 12 | 1 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| tax_rate | decimal | 5 | 1 |  |  |  |

