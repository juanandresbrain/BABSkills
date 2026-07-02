# dbo.item_group

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| item_group_id | int | 4 | 0 | YES |  |  |
| item_group_code | nvarchar | 44 | 0 |  |  |  |
| item_group_description | nvarchar | 60 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [USICOAL: dbo.RPT_GET_ITEM_GROUP](../../StoredProcedures/USICOAL/dbo.RPT_GET_ITEM_GROUP.md)

