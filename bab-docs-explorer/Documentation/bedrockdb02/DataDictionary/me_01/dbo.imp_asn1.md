# dbo.imp_asn1

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_asn_id | decimal | 9 | 0 | YES |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| shipment_ref_no | nvarchar | 60 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_inter_id_qualifier | nvarchar | 4 | 1 |  |  |  |
| vendor_inter_id_code | nvarchar | 30 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| container_type_code | nvarchar | 6 | 1 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| pro_bill_no | nvarchar | 60 | 1 |  |  |  |
| bol | nvarchar | 40 | 1 |  |  |  |
| imp_file_name | nvarchar | 400 | 0 |  |  |  |

