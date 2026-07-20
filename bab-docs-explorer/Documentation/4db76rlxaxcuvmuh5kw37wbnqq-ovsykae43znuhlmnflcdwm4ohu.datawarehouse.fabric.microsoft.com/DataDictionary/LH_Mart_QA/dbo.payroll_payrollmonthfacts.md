# dbo.payroll_payrollmonthfacts

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| adj_actual | decimal | 9 | 1 |  |  |  |
| adj_earned | decimal | 9 | 1 |  |  |  |
| actual | decimal | 9 | 1 |  |  |  |
| earned | decimal | 9 | 1 |  |  |  |
| loaded_date | datetime2 | 8 | 1 |  |  |  |
| updated_date | datetime2 | 8 | 1 |  |  |  |
