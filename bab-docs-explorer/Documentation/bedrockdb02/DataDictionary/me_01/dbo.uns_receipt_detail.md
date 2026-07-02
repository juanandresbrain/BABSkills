# dbo.uns_receipt_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| uns_receipt_detail_id | decimal | 9 | 0 | YES |  |  |
| unsolicited_receipt_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| unit_cost | decimal | 9 | 1 |  |  |  |
| units_received | int | 4 | 1 |  |  |  |
| total_retail_received | decimal | 9 | 1 |  |  |  |
| total_cost_received | decimal | 9 | 1 |  |  |  |
| total_val_retail_received | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)

