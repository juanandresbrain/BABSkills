# dbo.me_01_po_shipment

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_shipment_id | int | 4 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| expected_receipt_date | datetime2 | 8 | 1 |  |  |  |
| estimated_shipment_percent | decimal | 5 | 1 |  |  |  |
| sourcing_line_ship_id | int | 4 | 1 |  |  |  |
| sourcing_line_number | int | 4 | 1 |  |  |  |
| storepack_defn_released_flag | bit | 1 | 1 |  |  |  |
| country_id | decimal | 9 | 1 |  |  |  |
| carrier_id | int | 4 | 1 |  |  |  |
| ship_via_id | int | 4 | 1 |  |  |  |
| fob_description | varchar | 8000 | 1 |  |  |  |
