# dbo.vendor_review_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_review_parameter_id | int | 4 | 0 | YES |  |  |
| vendor_review_location_id | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| effective_inventory_time_frame | int | 4 | 0 |  |  |  |
| suspend_reorder_from_vendor | bit | 1 | 0 |  |  |  |
| reorder_suspension_from | smalldatetime | 4 | 1 |  |  |  |
| reorder_suspension_to | smalldatetime | 4 | 1 |  |  |  |

