# dbo.post_sql

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| posting_step | smallint | 2 | 0 | YES |  |  |
| sequence_number | tinyint | 1 | 0 | YES |  |  |
| dbms_type | tinyint | 1 | 0 | YES |  |  |
| sql_statement | nvarchar | -1 | 0 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |

