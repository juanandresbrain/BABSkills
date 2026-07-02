# dbo.shrink_adjustment_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shrink_adjustment_detail_id | decimal | 9 | 0 | YES |  |  |
| shrink_adjustment_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_shrink_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_shrink_adj_documents_$sp.md)
- [me_01: dbo.spMerchandisingNightlySyncPostSummary](../../StoredProcedures/me_01/dbo.spMerchandisingNightlySyncPostSummary.md)
- [me_01: dbo.spMerchandisingOutputUKstoreMHUshrink](../../StoredProcedures/me_01/dbo.spMerchandisingOutputUKstoreMHUshrink.md)
- [me_01: dbo.spMerchandisingSelectMultipleShrinkDocs](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMultipleShrinkDocs.md)
- [me_01: dbo.spMerchandisingSelectShrinkAdjustmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkAdjustmentSummary.md)

