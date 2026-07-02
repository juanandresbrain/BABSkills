# dbo.xref_info

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_ref | nvarchar | 256 | 0 |  |  |  |
| object_ref_type | nvarchar | 256 | 0 |  |  |  |
| event | nvarchar | 256 | 0 |  |  |  |
| referenced_in | nvarchar | 256 | 0 |  |  |  |
| ref_in_type | nvarchar | 256 | 0 |  |  |  |
| pbl | nvarchar | 256 | 0 |  |  |  |
| application | nvarchar | 128 | 0 |  |  |  |
| scope | nvarchar | 2 | 1 |  |  |  |
| category | nvarchar | 64 | 1 |  |  |  |
| short_event | nvarchar | 256 | 1 |  |  |  |

