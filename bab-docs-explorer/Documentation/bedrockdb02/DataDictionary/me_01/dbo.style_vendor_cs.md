# dbo.style_vendor_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_vendor_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| primary_vendor_flag | bit | 1 | 0 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |

