# Staging.CRMRewardTransaction

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reward_transaction_id | int | 4 | 0 |  |  |  |
| customer_id | int | 4 | 0 |  |  |  |
| transaction_id | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| reward_category | nchar | 2 | 0 |  |  |  |
| points_posted | numeric | 5 | 0 |  |  |  |
| points_available | numeric | 5 | 0 |  |  |  |
| reason_type_code | nchar | 20 | 1 |  |  |  |
| comments | nvarchar | 60 | 1 |  |  |  |
| total_net_retail | money | 8 | 0 |  |  |  |
| total_net_units | real | 4 | 0 |  |  |  |
| regular_points | numeric | 5 | 0 |  |  |  |
| header_bonus_points | numeric | 5 | 0 |  |  |  |
| detail_bonus_points | numeric | 5 | 0 |  |  |  |
| tender_bonus_points | numeric | 5 | 0 |  |  |  |
| date_points_posted | smalldatetime | 4 | 0 |  |  |  |
| reference_no | bigint | 8 | 1 |  |  |  |
| original_reward_tran_id | int | 4 | 1 |  |  |  |
| transaction_time | smalldatetime | 4 | 1 |  |  |  |
| total_net_retail_central | money | 8 | 1 |  |  |  |
| exchange_rate | numeric | 9 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| redemption_reversed | bit | 1 | 1 |  |  |  |
| amount | money | 8 | 1 |  |  |  |
| country_code | char | 3 | 0 |  |  |  |
