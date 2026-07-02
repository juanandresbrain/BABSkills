# dbo.location_eom_parameter

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| last_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| site_name | nvarchar | 510 | 1 |  |  |  |
| site_guid | varchar | 37 | 1 |  |  |  |
| service_uri | nvarchar | 510 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| ftp_uri | nvarchar | 1000 | 1 |  |  |  |
| ftp_username | nvarchar | 100 | 1 |  |  |  |
| ftp_password | nvarchar | 100 | 1 |  |  |  |
| last_ib_on_order_id | decimal | 9 | 1 |  |  |  |
| last_ib_allocation_id | decimal | 9 | 1 |  |  |  |
| last_ib_future_inventory_reserve_id | bigint | 8 | 1 |  |  |  |
| last_im_replication_queue_id | decimal | 9 | 1 |  |  |  |
| website_uri | nvarchar | 510 | 1 |  |  |  |

