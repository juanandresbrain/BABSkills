# dbo.ScorecardCharts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| weekending_date_key | int | 4 | 1 |  |  |  |
| comp_y_n | int | 4 | 1 |  |  |  |
| ty_date_key | int | 4 | 1 |  |  |  |
| ty_running_7_sales | decimal | 9 | 1 |  |  |  |
| ty_running_7_gaap_sales | decimal | 9 | 1 |  |  |  |
| ty_running_7_sales_comp | decimal | 9 | 1 |  |  |  |
| ty_running_7_gaap_sales_comp | decimal | 9 | 1 |  |  |  |
| ly_running_7_sales | decimal | 9 | 1 |  |  |  |
| ly_running_7_gaap_sales | decimal | 9 | 1 |  |  |  |
| ty_running_7_plan | decimal | 9 | 1 |  |  |  |
| ty_running_7_gaap_plan | decimal | 9 | 1 |  |  |  |
| ty_running_OSAT_sc | int | 4 | 1 |  |  |  |
| ty_running_OSAT_res | int | 4 | 1 |  |  |  |
| ty_running_BBW_sc | int | 4 | 1 |  |  |  |
| ty_running_BBW_res | int | 4 | 1 |  |  |  |
| osat_run | int | 4 | 1 |  |  |  |
| BABW_OSAT_Goal | decimal | 5 | 1 |  |  |  |
