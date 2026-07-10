# Staging.CRMPointExpiration

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_id | int | 4 | 0 |  |  |  |
| last_date_points_expired | smalldatetime | 4 | 1 |  |  |  |
| last_no_points_expired | numeric | 9 | 1 |  |  |  |
| country_code | nvarchar | 6 | 1 |  |  |  |
