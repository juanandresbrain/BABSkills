# dbo.imp_po

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_po_id | decimal | 9 | 0 | YES |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| po_no | nvarchar | 40 | 1 |  |  |  |
| po_description | nvarchar | 120 | 1 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| po_type | smallint | 2 | 1 |  |  |  |
| predistribution_type | smallint | 2 | 1 |  |  |  |
| buyer_code | nvarchar | 40 | 1 |  |  |  |
| print_flag | bit | 1 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |
| po_date | smalldatetime | 4 | 0 |  |  |  |
| po_delivery_date | smalldatetime | 4 | 0 |  |  |  |
| in_warehouse_date | smalldatetime | 4 | 0 |  |  |  |
| receiving_location | nvarchar | 40 | 1 |  |  |  |
| terms_code | nvarchar | 30 | 1 |  |  |  |
| terms_as_of | smalldatetime | 4 | 1 |  |  |  |
| ticket_source | smallint | 2 | 1 |  |  |  |
| ticket_status | smallint | 2 | 1 |  |  |  |
| edi_flag | bit | 1 | 1 |  |  |  |
| country_code | nvarchar | 6 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |
| import_order_flag | bit | 1 | 1 |  |  |  |
| new_store_flag | bit | 1 | 1 |  |  |  |
| special_order_flag | bit | 1 | 1 |  |  |  |
| replenishment_order_flag | bit | 1 | 1 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_document_no | nvarchar | 40 | 1 |  |  |  |
| blanket_po_number | nvarchar | 40 | 1 |  |  |  |
| reference_po_no | nvarchar | 40 | 1 |  |  |  |
| multiple_shipments_flag | bit | 1 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| agent | nvarchar | 120 | 1 |  |  |  |
| consolidator | nvarchar | 120 | 1 |  |  |  |
| gen_tkts_frm_warehouse | smallint | 2 | 1 |  |  |  |
| transaction_set_purpose_code | nvarchar | 4 | 1 |  |  |  |
| acknowledgement_type | nvarchar | 4 | 1 |  |  |  |
| vendor_interchange_id_qual | nvarchar | 4 | 1 |  |  |  |
| vendor_interchange_id_code | nvarchar | 30 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| position_id | decimal | 9 | 1 |  |  |  |
| terms_id | smallint | 2 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| country_id | decimal | 9 | 1 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| release_to_dc_flag | bit | 1 | 0 |  |  |  |
| store_pack_flag | bit | 1 | 0 |  |  |  |

