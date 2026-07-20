# dbo.me_01_vendor

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_id | decimal | 9 | 1 |  |  |  |
| vendor_code | varchar | 8000 | 1 |  |  |  |
| vendor_name | varchar | 8000 | 1 |  |  |  |
| alternate_vendor_code | varchar | 8000 | 1 |  |  |  |
| country_id | decimal | 9 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| terms_id | int | 4 | 1 |  |  |  |
| gl_distribution_set_id | int | 4 | 1 |  |  |  |
| vendor_parameter_set_id | int | 4 | 1 |  |  |  |
| reference_set_id | int | 4 | 1 |  |  |  |
| remit_to_vendor_id | int | 4 | 1 |  |  |  |
| imat_able_flag | bit | 1 | 1 |  |  |  |
| import_flag | bit | 1 | 1 |  |  |  |
| requires_vendor_upc_flag | bit | 1 | 1 |  |  |  |
| rtv_option | int | 4 | 1 |  |  |  |
| rtv_acknowledgement_req_flag | bit | 1 | 1 |  |  |  |
| asn_auto_receive_flag | bit | 1 | 1 |  |  |  |
| fob_description | varchar | 8000 | 1 |  |  |  |
| ship_via_id | int | 4 | 1 |  |  |  |
| carrier_id | int | 4 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| vendor_interchange_id_qual | varchar | 8000 | 1 |  |  |  |
| vendor_interchange_id_code | varchar | 8000 | 1 |  |  |  |
| retailer_interchange_id_qual | varchar | 8000 | 1 |  |  |  |
| retailer_interchange_id_code | varchar | 8000 | 1 |  |  |  |
| send_location_id_qual | varchar | 8000 | 1 |  |  |  |
| send_location_id_code | varchar | 8000 | 1 |  |  |  |
| receive_location_id_qual | varchar | 8000 | 1 |  |  |  |
| edi_able_flag | bit | 1 | 1 |  |  |  |
| edi_850_dtm_cancel_after_flag | bit | 1 | 1 |  |  |  |
| edi_850_dtm_delivery_req_flag | bit | 1 | 1 |  |  |  |
| edi_850_dtm_effective_flag | bit | 1 | 1 |  |  |  |
| edi_850_ctp_msr_flag | bit | 1 | 1 |  |  |  |
| edi_850_ctp_resale_flag | bit | 1 | 1 |  |  |  |
| interchange_control_number | decimal | 5 | 1 |  |  |  |
| group_control_number | decimal | 5 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 1 |  |  |  |
| allow_customer_shipment_flag | bit | 1 | 1 |  |  |  |
| min_on_order_cost_bulk_xdock | decimal | 9 | 1 |  |  |  |
| min_on_order_cost_dropship | decimal | 9 | 1 |  |  |  |
| supports_store_pack | bit | 1 | 1 |  |  |  |
| interface_to_wholesale | bit | 1 | 1 |  |  |  |
| asn_auto_generate_po_rcpt_status | int | 4 | 1 |  |  |  |
| track_in_transit_flag | bit | 1 | 1 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 1 |  |  |  |
| allow_direct_shipments_to_customer_flag | bit | 1 | 1 |  |  |  |
| allow_customer_back_order | int | 4 | 1 |  |  |  |
