# dbo.imp_out_xfer_bak

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_out_xfer_id | decimal | 9 | 0 |  |  |  |
| action | char | 1 | 0 |  |  |  |
| xfer_no | varchar | 20 | 0 |  |  |  |
| description | varchar | 60 | 1 |  |  |  |
| imrd_no | varchar | 20 | 1 |  |  |  |
| from_location_code | varchar | 20 | 0 |  |  |  |
| from_location_address_type | varchar | 20 | 1 |  |  |  |
| to_location_code | varchar | 20 | 0 |  |  |  |
| to_location_address_type | varchar | 20 | 1 |  |  |  |
| ship_via_code | varchar | 2 | 1 |  |  |  |
| carrier_code | varchar | 4 | 1 |  |  |  |
| packed_by | varchar | 60 | 1 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| bill_of_lading | varchar | 20 | 1 |  |  |  |
| unit_weight_code | varchar | 10 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| container_type_code | varchar | 3 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| reason_code | varchar | 5 | 0 |  |  |  |
| cross_ref | varchar | 20 | 1 |  |  |  |
| routed_through_warehouse | char | 1 | 1 |  |  |  |
| warehouse | varchar | 20 | 1 |  |  |  |
| grouping_label | varchar | 20 | 1 |  |  |  |
| imp_file_name | varchar | 200 | 0 |  |  |  |
| transaction_no | varchar | 20 | 1 |  |  |  |
| register_no | varchar | 20 | 1 |  |  |  |
| out_xfer_status | char | 1 | 0 |  |  |  |

