# dbo.oim_po_receipt

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_po_receipt_id | numeric | 9 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| po_no | nvarchar | 40 | 0 |  |  |  |
| advance_shipping_notice_no | nvarchar | 40 | 1 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| weight | numeric | 9 | 1 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| container_type_code | nvarchar | 6 | 1 |  |  |  |
| bol_total_cartons | int | 4 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| packing_list_no | nvarchar | 40 | 1 |  |  |  |
| packing_list_date | smalldatetime | 4 | 1 |  |  |  |
| pro_bill_no | nvarchar | 60 | 1 |  |  |  |
| appointment_no | nvarchar | 12 | 1 |  |  |  |
| freight_amount | numeric | 9 | 1 |  |  |  |
| payment_method | int | 4 | 1 |  |  |  |
| reason_code | nvarchar | 10 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
