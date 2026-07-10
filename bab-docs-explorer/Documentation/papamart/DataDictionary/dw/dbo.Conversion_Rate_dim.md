# dbo.Conversion_Rate_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| conversion_rate_key | int | 4 | 0 | YES |  |  |
| date_key | int | 4 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| ca_to_us | float | 8 | 1 |  |  |  |
| us_to_ca | float | 8 | 1 |  |  |  |
