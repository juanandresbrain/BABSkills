# dbo.ticket_format

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ticket_format_id | decimal | 9 | 0 | YES |  |  |
| ticket_format_code | nvarchar | 4 | 0 |  |  |  |
| ticket_format_description | nvarchar | 80 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_merch_hierarchies_characteristics_$sp](../../StoredProcedures/me_01/dbo.rpt_merch_hierarchies_characteristics_$sp.md)

