# dbo.discrepancy_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| discrepancy_queue_id | decimal | 9 | 0 | YES |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| asn_shipment_ref_no | nvarchar | 60 | 0 |  |  |  |
| asn_document_no | nvarchar | 40 | 0 |  |  |  |
| por_document_no | nvarchar | 40 | 0 |  |  |  |
| po_no | nvarchar | 40 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| size_code | nvarchar | 34 | 0 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| discrepancy_qty | int | 4 | 0 |  |  |  |

