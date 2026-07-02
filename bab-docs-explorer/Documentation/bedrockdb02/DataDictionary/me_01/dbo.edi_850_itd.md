# dbo.edi_850_itd

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 0 |  |  |  |
| itd02_terms_basis_date_code | tinyint | 1 | 1 |  |  |  |
| itd03_terms_discount_percent | decimal | 5 | 1 |  |  |  |
| itd04_terms_discount_due_date | smalldatetime | 4 | 1 |  |  |  |
| itd05_terms_discount_days_due | smallint | 2 | 1 |  |  |  |
| itd06_terms_net_due_date | smalldatetime | 4 | 1 |  |  |  |
| itd07_terms_net_days | smallint | 2 | 1 |  |  |  |
| itd09_terms_deferred_due_date | smalldatetime | 4 | 1 |  |  |  |
| itd12_terms_description | varchar | 80 | 1 |  |  |  |

