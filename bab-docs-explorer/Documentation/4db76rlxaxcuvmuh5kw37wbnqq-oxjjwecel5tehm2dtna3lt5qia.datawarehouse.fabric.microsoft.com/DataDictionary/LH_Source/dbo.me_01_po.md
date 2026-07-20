# dbo.me_01_po

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| print_flag | bit | 1 | 1 |  |  |  |
| edi_flag | bit | 1 | 1 |  |  |  |
| import_order_flag | bit | 1 | 1 |  |  |  |
| special_order_flag | bit | 1 | 1 |  |  |  |
| multiple_shipments_flag | bit | 1 | 1 |  |  |  |
| cancellation_exemption_flag | bit | 1 | 1 |  |  |  |
| allocation_completed_flag | bit | 1 | 1 |  |  |  |
| new_store_flag | bit | 1 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| ticket_source | int | 4 | 1 |  |  |  |
| ticket_status | int | 4 | 1 |  |  |  |
| gen_tkts_frm_warehouse | bit | 1 | 1 |  |  |  |
| last_modified | datetime2 | 8 | 1 |  |  |  |
| position_id | decimal | 9 | 1 |  |  |  |
| ship_via_id | int | 4 | 1 |  |  |  |
| fob_description | varchar | 8000 | 1 |  |  |  |
| country_id | decimal | 9 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| terms_id | int | 4 | 1 |  |  |  |
| po_no | varchar | 8000 | 1 |  |  |  |
| po_description | varchar | 8000 | 1 |  |  |  |
| po_type | int | 4 | 1 |  |  |  |
| predistribution_type | int | 4 | 1 |  |  |  |
| create_date | datetime2 | 8 | 1 |  |  |  |
| system_cancel_date | datetime2 | 8 | 1 |  |  |  |
| order_date | datetime2 | 8 | 1 |  |  |  |
| terms_as_of | datetime2 | 8 | 1 |  |  |  |
| po_discount_last_modified | datetime2 | 8 | 1 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |
| po_status | int | 4 | 1 |  |  |  |
| approval_status | int | 4 | 1 |  |  |  |
| blanket_po_number | varchar | 8000 | 1 |  |  |  |
| release_number | int | 4 | 1 |  |  |  |
| approval_category | int | 4 | 1 |  |  |  |
| carrier_id | int | 4 | 1 |  |  |  |
| number_of_releases | int | 4 | 1 |  |  |  |
| printed_status | int | 4 | 1 |  |  |  |
| edi_status | int | 4 | 1 |  |  |  |
| cancellation_reason | int | 4 | 1 |  |  |  |
| source | int | 4 | 1 |  |  |  |
| external_system_name | varchar | 8000 | 1 |  |  |  |
| external_document_no | varchar | 8000 | 1 |  |  |  |
| reference_po_no | varchar | 8000 | 1 |  |  |  |
| po_cancellation_reason_id | decimal | 5 | 1 |  |  |  |
| agent | varchar | 8000 | 1 |  |  |  |
| consolidator | varchar | 8000 | 1 |  |  |  |
| actual_cancel_date | datetime2 | 8 | 1 |  |  |  |
| reinstated_flag | bit | 1 | 1 |  |  |  |
| from_delivery_date | datetime2 | 8 | 1 |  |  |  |
| to_delivery_date | datetime2 | 8 | 1 |  |  |  |
| validate_order_multiple | bit | 1 | 1 |  |  |  |
| release_to_dc_flag | bit | 1 | 1 |  |  |  |
| split_release_po_flag | bit | 1 | 1 |  |  |  |
| total_net_final_imu_percent | decimal | 9 | 1 |  |  |  |
| storepack_defns_ready_flag | bit | 1 | 1 |  |  |  |
| generated_by_wholesale_distro | bit | 1 | 1 |  |  |  |
| line_shipment_cost_factors_flag | bit | 1 | 1 |  |  |  |
