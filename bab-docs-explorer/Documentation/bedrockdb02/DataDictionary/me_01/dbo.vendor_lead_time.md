# dbo.vendor_lead_time

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_lead_time_id | T_ID | 16 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| inhouse_review_time | smallint | 2 | 0 |  |  |  |
| lead_time | smallint | 2 | 0 |  |  |  |
| additional_days_supply | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

