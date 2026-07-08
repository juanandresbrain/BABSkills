# dbo.store_list

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_list_id | numeric | 9 | 0 | YES |  |  |
| store_list_name | nvarchar | 60 | 0 |  |  |  |
| source | nchar | 2 | 0 |  |  |  |
| no_of_levels | tinyint | 1 | 0 |  |  |  |
| selection_tag | nvarchar | 40 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
