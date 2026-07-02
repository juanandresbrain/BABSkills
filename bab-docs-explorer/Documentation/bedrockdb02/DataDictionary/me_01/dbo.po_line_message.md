# dbo.po_line_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_line_message_id | smallint | 2 | 0 |  |  |  |
| message_type_id | decimal | 9 | 0 |  | YES |  |
| message | nvarchar | 510 | 1 |  |  |  |
| po_line_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_po_messages_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_messages_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)

