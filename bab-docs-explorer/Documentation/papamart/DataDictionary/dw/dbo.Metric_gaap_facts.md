# dbo.Metric_gaap_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| metric_gaap_facts_key | int | 4 | 0 | YES |  |  |
| metric_dim_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| amount | decimal | 9 | 1 |  |  |  |
| ly_date_key | int | 4 | 1 |  |  |  |
| ly_amount | decimal | 9 | 1 |  |  |  |
