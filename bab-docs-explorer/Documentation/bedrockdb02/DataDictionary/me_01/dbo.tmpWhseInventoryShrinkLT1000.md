# dbo.tmpWhseInventoryShrinkLT1000

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 9 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| MerchQty | int | 4 | 1 |  |  |  |
| Whseqty | int | 4 | 1 |  |  |  |
| shrinkqty | int | 4 | 1 |  |  |  |
| style_type | varchar | 5 | 0 |  |  |  |
| shrinkqty_distribution_multiple | int | 4 | 1 |  |  |  |

