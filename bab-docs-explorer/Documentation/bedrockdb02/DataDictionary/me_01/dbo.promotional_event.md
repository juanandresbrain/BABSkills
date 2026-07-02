# dbo.promotional_event

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | T_ID | 16 | 0 | YES |  |  |
| event_number | nvarchar | 40 | 1 |  |  |  |
| event_type | smallint | 2 | 0 |  |  |  |
| description | nvarchar | 120 | 1 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.add_promtional_event_$sp](../../StoredProcedures/me_01/dbo.add_promtional_event_$sp.md)
- [me_01: dbo.upd_promo_events_$sp](../../StoredProcedures/me_01/dbo.upd_promo_events_$sp.md)

