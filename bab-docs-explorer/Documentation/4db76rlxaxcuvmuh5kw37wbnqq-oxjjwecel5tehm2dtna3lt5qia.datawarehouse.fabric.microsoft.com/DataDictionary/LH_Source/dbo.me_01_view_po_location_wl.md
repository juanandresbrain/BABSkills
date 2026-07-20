# dbo.me_01_view_po_location_wl

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 1 |  |  |  |
| po_shipment_id | int | 4 | 1 |  |  |  |
| po_location_id | int | 4 | 1 |  |  |  |
| location_id | int | 4 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| location_name | varchar | 8000 | 1 |  |  |  |
| location_short_name | varchar | 8000 | 1 |  |  |  |
| location_type | int | 4 | 1 |  |  |  |
| total_loc_net_cost | float | 8 | 1 |  |  |  |
