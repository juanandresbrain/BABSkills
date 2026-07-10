# dbo.reward_certificate_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reward_certificate_key | int | 4 | 0 | YES |  |  |
| reward_certificate_code | varchar | 25 | 0 |  |  |  |
| first_earned_date_key | int | 4 | 1 |  |  |  |
| cert_value | decimal | 5 | 1 |  |  |  |
