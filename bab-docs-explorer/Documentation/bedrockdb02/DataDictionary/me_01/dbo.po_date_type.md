# dbo.po_date_type

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_date_type_id | decimal | 9 | 0 | YES |  |  |
| date_type_code | nvarchar | 6 | 0 |  |  |  |
| description | nvarchar | 120 | 0 |  |  |  |
| edi_support_flag | bit | 1 | 0 |  |  |  |
| print_on_po_flag | bit | 1 | 0 |  |  |  |
| sequence | smallint | 2 | 0 |  |  |  |
| mandatory_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_po_shipment_udds_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_shipment_udds_$sp.md)

