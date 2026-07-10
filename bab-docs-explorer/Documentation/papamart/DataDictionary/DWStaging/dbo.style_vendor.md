# dbo.style_vendor

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_vendor_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| primary_vendor_flag | bit | 1 | 0 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
