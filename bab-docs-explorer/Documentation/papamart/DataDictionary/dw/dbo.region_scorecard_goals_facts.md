# dbo.region_scorecard_goals_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| region_key | varchar | 255 | 0 |  |  |  |
| as_of_date_key | int | 4 | 0 |  |  |  |
| currency_key | int | 4 | 0 |  |  |  |
| hpg_goal | decimal | 9 | 1 |  |  |  |
| bags_goal | decimal | 5 | 1 |  |  |  |
| party_sales_percent_goal | decimal | 5 | 1 |  |  |  |
| skins_to_trans_goal | decimal | 5 | 1 |  |  |  |
| avg_skin_price_goal | decimal | 9 | 1 |  |  |  |
| sounds_to_skins_goal | decimal | 5 | 1 |  |  |  |
| shoes_to_skins_goal | decimal | 5 | 1 |  |  |  |
| FileLocation | varchar | 300 | 1 |  |  |  |
| ModifiedDateTime | datetime | 8 | 1 |  |  |  |
