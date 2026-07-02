# dbo.imp_out_xfer

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_out_xfer_id | decimal | 9 | 0 | YES |  |  |
| action | nchar | 2 | 0 |  |  |  |
| xfer_no | nvarchar | 40 | 0 |  |  |  |
| description | nvarchar | 120 | 1 |  |  |  |
| imrd_no | nvarchar | 40 | 1 |  |  |  |
| from_location_code | nvarchar | 40 | 0 |  |  |  |
| from_location_address_type | nvarchar | 40 | 1 |  |  |  |
| to_location_code | nvarchar | 40 | 0 |  |  |  |
| to_location_address_type | nvarchar | 40 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| packed_by | nvarchar | 120 | 1 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| bill_of_lading | nvarchar | 40 | 1 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| container_type_code | nvarchar | 6 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| reason_code | nvarchar | 10 | 0 |  |  |  |
| cross_ref | nvarchar | 40 | 1 |  |  |  |
| routed_through_warehouse | nchar | 2 | 1 |  |  |  |
| warehouse | nvarchar | 40 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| imp_file_name | nvarchar | 400 | 0 |  |  |  |
| transaction_no | nvarchar | 40 | 1 |  |  |  |
| register_no | nvarchar | 40 | 1 |  |  |  |
| out_xfer_status | char | 1 | 0 |  |  |  |

