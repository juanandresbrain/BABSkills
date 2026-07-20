# dbo.me_01_view_po_ship_udd_wl

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 1 |  |  |  |
| po_shipment_id | int | 4 | 1 |  |  |  |
| user_defined_date | datetime2 | 8 | 1 |  |  |  |
| po_date_type_id | decimal | 9 | 1 |  |  |  |
| date_type_code | varchar | 8000 | 1 |  |  |  |
| date_type_desc | varchar | 8000 | 1 |  |  |  |
