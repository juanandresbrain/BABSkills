# dbo.imp_merch_group_desc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_merch_group_desc_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nvarchar | 2 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| locale_identifier | smallint | 2 | 0 |  |  |  |
| hierarchy_group_label | nvarchar | 80 | 1 |  |  |  |
| hierarchy_group_short_label | nvarchar | 40 | 1 |  |  |  |
| plu_description | nvarchar | 80 | 1 |  |  |  |

