# dbo.imp_asn_sku1

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_asn_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_asn_id | decimal | 9 | 1 |  |  |  |
| action | nchar | 2 | 0 |  |  |  |
| shipment_ref_no | nvarchar | 60 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_inter_id_qualifier | nvarchar | 4 | 1 |  |  |  |
| vendor_inter_id_code | nvarchar | 30 | 1 |  |  |  |
| po_number | nvarchar | 40 | 1 |  |  |  |
| blanket_po_no | nvarchar | 40 | 1 |  |  |  |
| release_no | smallint | 2 | 1 |  |  |  |
| ship_to_location | nvarchar | 40 | 0 |  |  |  |
| selling_location_code | nvarchar | 40 | 1 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| vendor_style_code | nvarchar | 80 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |
| units_shipped | int | 4 | 0 |  |  |  |

