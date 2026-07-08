# dbo.oim_out_xfer

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_out_xfer_id | numeric | 9 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| inventory_move_request_no | nvarchar | 40 | 1 |  |  |  |
| from_location_id | smallint | 2 | 0 |  |  |  |
| from_loc_address_type_desc | nvarchar | 40 | 1 |  |  |  |
| to_location_id | smallint | 2 | 0 |  |  |  |
| to_loc_address_type_desc | nvarchar | 40 | 1 |  |  |  |
| routed_by_warehouse_flag | tinyint | 1 | 0 |  |  |  |
| warehouse_id | smallint | 2 | 1 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| begin_send_date | smalldatetime | 4 | 1 |  |  |  |
| end_send_date | smalldatetime | 4 | 1 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| packed_by | nvarchar | 120 | 1 |  |  |  |
| weight | numeric | 9 | 1 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| container_type_code | nvarchar | 6 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| bill_of_lading | nvarchar | 40 | 1 |  |  |  |
| cross_ref | nvarchar | 40 | 1 |  |  |  |
| reason_code | nvarchar | 10 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| initiated_by_host | tinyint | 1 | 0 |  |  |  |
