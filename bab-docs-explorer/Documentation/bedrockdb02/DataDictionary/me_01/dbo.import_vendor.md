# dbo.import_vendor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_vendor_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_name | nvarchar | 100 | 1 |  |  |  |
| country_code | nvarchar | 6 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| terms_code | nvarchar | 30 | 1 |  |  |  |
| requires_vendor_upc_flag | nchar | 2 | 1 |  |  |  |
| rtv_option | decimal | 5 | 1 |  |  |  |
| rtv_acknowledgement_req_flag | nchar | 2 | 1 |  |  |  |
| alternate_vendor_code | nvarchar | 40 | 1 |  |  |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| preferred_carrier_code | nvarchar | 8 | 1 |  |  |  |
| import_flag | nchar | 2 | 1 |  |  |  |
| cash_discount_percent | decimal | 5 | 1 |  |  |  |
| van# | decimal | 9 | 1 |  |  |  |
| vendor_interchange_id_qual | decimal | 5 | 1 |  |  |  |
| vendor_interchange_id_code | nvarchar | 30 | 1 |  |  |  |
| retailer_interchange_id_qual | decimal | 5 | 1 |  |  |  |
| retailer_interchange_id_code | nvarchar | 30 | 1 |  |  |  |
| send_location_id_qual | decimal | 5 | 1 |  |  |  |
| send_location_id_code | nvarchar | 30 | 1 |  |  |  |
| receive_location_id_qualifier | nvarchar | 4 | 1 |  |  |  |
| receive_code | nvarchar | 30 | 1 |  |  |  |
| active_flag | nchar | 2 | 1 |  |  |  |
| asn_auto_receive_flag | nchar | 2 | 1 |  |  |  |
| edi_850_dtm_after_flag | nchar | 2 | 1 |  |  |  |
| edi_850_dtm_delivery_req_flag | nchar | 2 | 1 |  |  |  |
| edi_850_dtm_effective_flag | nchar | 2 | 1 |  |  |  |
| edi_850_ctp_msr_flag | nchar | 2 | 1 |  |  |  |
| edi_850_ctp_resale_flag | nchar | 2 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| gl_distribution_set_code | nvarchar | 40 | 1 |  |  |  |
| vendor_parameter_set_code | nvarchar | 40 | 1 |  |  |  |
| reference_set_code | nvarchar | 40 | 1 |  |  |  |
| remit_to_vendor_code | nvarchar | 40 | 1 |  |  |  |
| imat_flow_code | nvarchar | 40 | 1 |  |  |  |
| address_name | nvarchar | 120 | 1 |  |  |  |
| address_line1 | nvarchar | 100 | 1 |  |  |  |
| address_line2 | nvarchar | 100 | 1 |  |  |  |
| address_city | nvarchar | 40 | 1 |  |  |  |
| address_state | nvarchar | 40 | 1 |  |  |  |
| address_country_code | nvarchar | 6 | 1 |  |  |  |
| address_zip_code | nvarchar | 30 | 1 |  |  |  |
| address_email | nvarchar | 120 | 1 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| allow_customer_shipment_flag | nchar | 2 | 1 |  |  |  |
| min_on_order_cost_bulk_xdock | decimal | 9 | 1 |  |  |  |
| min_on_order_cost_dropship | decimal | 9 | 1 |  |  |  |
| supports_store_pack | bit | 1 | 0 |  |  |  |
| interface_to_wholesale | bit | 1 | 0 |  |  |  |
| asn_auto_generate_po_rcpt_status | smallint | 2 | 1 |  |  |  |
| track_in_transit_flag | bit | 1 | 1 |  |  |  |

