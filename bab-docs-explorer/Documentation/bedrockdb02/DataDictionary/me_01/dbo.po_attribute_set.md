# dbo.po_attribute_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_attribute_set_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| attribute_set_id | decimal | 9 | 0 |  | YES |  |
| attribute_id | decimal | 9 | 0 |  | YES |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_po_attributes_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_attributes_$sp.md)

