# dbo.tmp_DDC_PO_Export

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | nvarchar | 40 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_name | nvarchar | 100 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| ItemDesc | nvarchar | 8000 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| EndDeliverDateTime | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)

